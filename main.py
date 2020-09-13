import os
import re
import sys
import json
import shutil
import sqlite3
import requests
import logging
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup as bs
from markdownify import markdownify as md

# initializing logger
log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))
# disable urllib3 logging
logging.getLogger("urllib3").setLevel(logging.WARNING)

config = json.load(open('config.json'))

Archives = Path(config["Archives"])
conn = sqlite3.connect(config["SQLite"])
cursor = conn.cursor()

WeRssApi = "https://wealert2.vux.li/api/v3/developers/subscribes/{RSSID}?token={Token}"
WeRssUrl = WeRssApi.format(RSSID=config["RSSID"], Token=config["Token"])

SHORT_LENGTH = 64
LONG_LENGTH = 512
DB_TABLE_NAME = "Articles"
DB_TABLE_SCHEMA = "{name}( \
    author varchar({short}), \
    content_iid varchar({short}), \
    is_original varchar({short}), \
    idx varchar({short}), \
    mid varchar({short}), \
    picture varchar({long}), \
    posted_at varchar({short}), \
    source_url varchar({long}), \
    summary varchar({long}), \
    title varchar({long}), \
    type varchar({short}), \
    url varchar({long}) \
)".format(
    name=DB_TABLE_NAME, 
    short=SHORT_LENGTH, 
    long=LONG_LENGTH
)

# remove invalid tags 
# when converting html to markdown
invalid_tags = ['span']

def download(url, outdir):
    fname = ''
    r = requests.get(url, stream=True)
    if "Content-Disposition" in r.headers.keys():
        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]

    with (outdir/fname).open('wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

def fixWxHtmlImg(soup):
    # add src attribute to img tag
    for img in soup.find_all("img"):
        if "data-src" in img:
            img["src"] = img["data-src"]
    
def removeInvalidTags(soup):
    # remove invalid tags but keep content
    for tag in invalid_tags:
        for match in soup.find_all(tag):
            match.replaceWithChildren()

def fixWxHtml(soup):
    # fix wechat html
    fixWxHtmlImg(soup)
    removeInvalidTags(soup)
    return soup.prettify()

def getPaperPdf(soup, outdir):
    # get paper pdf link
    stub = soup.find(text=re.compile(".*PDF(:|：)"))
    if not stub: return

    ptags = stub.parent.find_next_siblings('p')
    paper = ptags[0].text.strip()
    if not paper.endswith('.pdf'): return

    download(paper, outdir)
 
def getWeRssDatas():
    # get werss data
    resp = requests.get(WeRssUrl)
    obj = json.loads(resp.text)
    lists = obj["data"]["list"]
    return lists

def dbCreateTable():
    # sqlite create table
    cursor.execute("create table if not exists " + DB_TABLE_SCHEMA)

def dbInsertRow(feed):
    # insert row to sqlite db
    row = feed.copy()
    del row["content"]

    cols = ', '.join('"{}"'.format(col) for col in row.keys())
    vals = ', '.join('"{}"'.format(col) for col in row.values())
    data = '"{0}" ({1}) values ({2})'.format(DB_TABLE_NAME, cols, vals)

    sql = 'insert into ' + data
    cursor.execute(sql)

def dbExists(feed):
    # check row exists in sqlite db
    sql = "select exists(select 1 from {table} where title='{title}')".format(
        table=DB_TABLE_NAME, title=feed['title'])     

    cursor.execute(sql)
    return True if cursor.fetchone()[0] else False

def genMarkdown(html, outdir):
    # convert html to markdown and dump
    # TODO: fix link contains '\_'
    content = md(html)
    output = outdir / 'README.md'
    with output.open('w') as fp:
        fp.write(content)

def genHtml(html, outdir):
    # dump html
    output = outdir / 'source.html'
    with output.open('w') as fp:
        fp.write(html)

def parseFeed(feed):
    # parse, fix and dump html
    
    # print(feed["title"])
    outdir = Archives / feed["title"]
    if outdir.exists(): return
    else: outdir.mkdir(parents=True)

    soup = bs(feed["content"], "html.parser")

    html = fixWxHtml(soup)
    genHtml(html, outdir)
    genMarkdown(html, outdir)
    # getPaperPdf(soup, outdir)

def clean():
    # close sqlite db and push to github
    conn.commit()
    cursor.close()

def main():
    dbCreateTable()
    feeds = getWeRssDatas()
    for feed in feeds:
        if dbExists(feed): 
            continue
        parseFeed(feed)
        dbInsertRow(feed)
    clean()
    
if __name__ == '__main__':
    main()
