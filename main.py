import json
import requests
import re
import os
import shutil
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup as bs
#import html2markdown as h2m
from markdownify import markdownify as md

Token = "ddaf9e31-bad4-4cae-9714-bf81604fe4c2"
RSSID = "6888bc4a-b31c-48c6-a42f-9ee3a5f4d0d4"
WeRssApi = "https://wealert2.vux.li/api/v3/developers/subscribes/{RSSID}?token={Token}"
WeRssUrl = WeRssApi.format(RSSID=RSSID, Token=Token)

invalid_tags = ['span']




def download(url, outdir):
    print("downloading", url, "...")
    fname = ''
    r = requests.get(url, stream=True)
    if "Content-Disposition" in r.headers.keys():
        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]

    with (outdir/fname).open('wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

def fixWxHtmlImg(html):
    soup = bs(html, "html.parser")
    for img in soup.find_all("img"):
        # add src attribute
        img["src"] = img["data-src"]

    # remove invalid tags but keep content
    for tag in invalid_tags:
        for match in soup.find_all(tag):
            match.replaceWithChildren()

    paper_link = ''
    stub = soup.find(text=re.compile(".*PDF(:|：)"))
    if stub:
        ptags = stub.parent.find_next_siblings('p')
        paper = ptags[0].text.strip()
        if paper.endswith('.pdf'):
            paper_link = paper

    return soup.prettify(), paper_link

def gitpush():
    os.system("git add -A")
    os.system('git commit -m "GoSSIP-Bot Sync: {}"'.format(datetime.now()))
    os.system("git push origin master")

def main():
    response = requests.get(WeRssUrl)
    respObj = json.loads(response.text)
    datalist = respObj["data"]["list"]

    for metadata in datalist:
        title = metadata["title"]

        html, paper = fixWxHtmlImg(metadata["content"])
        # TODO: fix link contains '\_'
        content = md(html)
        outdir = Path("archives") / title
        if outdir.exists(): continue

        outdir.mkdir(parents=True)
        # if paper: download(paper, outdir)
        output = outdir / 'README.md'
        with output.open('w') as fp:
            fp.write(content)
            
    gitpush()

if __name__ == '__main__':
    main()