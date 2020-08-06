 今天向大家介绍一篇ICSE 2020会议的学术论文，该论文讨论了移动app中常用的分析统计组件的配置不当导致的隐私破坏问题 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0FWpzw3V8iaUZFeeXADDUHSicHzBQDwomibrrzlPdQqNu3WqWRkMPib8DmRQ/640?wx_fmt=png) 

    
 

  作者主要关注的third-party analytic services（例如Google Analytics）能够从用户的设备上搜集相关信息，这些服务往往还会使用personally identifiable information (PII) 来标记用户，然而这样的做法带来的问题是对用户身份的去匿名化，从而导致隐私破坏。作者开发了一款名为PAMDroid的工具，对Google Play上排名前1000的app进行了分析，发现其中有120个app中的analytic service均使用了PII且没有对这类信息加密，作者还人工去分析了所使用的analytic services的隐私数据使用策略文档，发现27个app中对PII的使用实际上违反了隐私数据使用策略文档。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0F1KpVicALWaJWjZ6F28CSxV8cAEWbDdsypPeegMksXibalYXMzViaAvQNg/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0FRfRiaLvPMud7JqV7ZLkqQmxicqZMR7PuhUQyWSibBHBg4LztOYj5rpCsg/640?wx_fmt=png) 

    
 

  具体地，作者发现Android ID、email、username和imei这类信息常常被analytic services用作PII： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0FibwdVsTrM5LFfqvTK38FrTtruV1h2X2ibSe2mlSSZAfR6xBttVg8C7Jw/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0FNiaWkJbhhPkzYgr0NT9fYoeD9uyjfeGay1GibTPtACWxJiadmkEBODf9Q/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0F4oVKe0aLaia8gzvhW00ydibHvZlSuEuyfLNITmwHcDUGt9BGp3sibafvA/640?wx_fmt=png) 

  作者的进一步研究表明： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0F4gI7rpic11JtmZiccPeGSnuR9iaMvZDym9BR9UibNpZHxZJo3Vls1riasCQ/640?wx_fmt=png) 

  可以看出，如果PII被搜集了，服务商很容易定位到用户： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiclcLOqE4WxrnyVueb97G0FXiary3Acr0E2bwqic7CUwicYytRoiaicjK73j63r0TTyficXpnia10ODytiaGQ/640?wx_fmt=png) 

  鉴于国内最近严打app侵犯用户隐私，这类问题尤其应该引起大家的关注~   
 

    
 

  论文PDF： 

  http://galadriel.cs.utsa.edu/~rslavin/publications/icse20.pdf 

