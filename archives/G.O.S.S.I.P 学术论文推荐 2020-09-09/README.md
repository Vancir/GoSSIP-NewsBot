 今天推荐一篇发表在USENIX Security 2020会议上关于Android app上Network Security Policy部署情况大规模分析的论文（其中第二作者8月底 在twitter 上宣布放弃自由生活，加入工业界--CISCO Talos team，并且抒发了一大通感想） 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72EvkTLic4RA3dnDIc9Cq1r596F9L4LqK8ZhHN2QR5tZlQC3C0L9ic0yxltDg/640?wx_fmt=png) 

  自Android6.0以来，谷歌进一步推行“HTTPS everywhere”计划，谷歌推出了Network Security Policy（后面简称NSP）机制，该机制允许开发者制定复杂的安全策略以保护app的网络安全。 

  作者首先描述了NSP的细节。NSP以XML文件形式进行配置，其可以配置的策略包括：Cleartext，用于设置允许明文的协议（如,HTTP、FTP等）；Certificate Pinning，用于配置证书固定；KeyStore and CAs用于指定安全连接时受信任的KeyStore；Debug，用于帮助开发人员调试策略的实现。NSP有默认的配置文件用于没有配置NSP的APP，且随着Android版本的提高而变得更加严格。 

  细粒度的策略可能会使开发人错误配置NSP，作者接下来讨论了三个可能会发生的错误。 

  *   Allow Cleartext.   
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72EvkgABCEQWbELSlGcTjEI8l1nlU9ruwOfM1H15r1picPzEfjHWeu5P0SdA/640?wx_fmt=png) 

    
 

 
 *   Certificate Pinning Override.   
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72Evkiahal0Wn144zMWJ8tT68gYapTGYXfBVGumEqGUbIWvH71tHSZyDEQKg/640?wx_fmt=png) 

 
     
 

  *   SilentMan-In-The-Middle.   
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72Evkqlt28LGDBdvWe4lS4j9ADL6nib2KJgazvvMMvy48jMxLEqXtvbZHfuQ/640?wx_fmt=png) 

 
   基于此，作者在2019年6月和7月期间分析了125,419个Android应用程序。作者发现只有16,332个app定义了NSP，而超过97%的app通过定义NSP以允许明文协议。由于从2019年11月开始，Google更改了一些与NSP相关的重要默认值（特别是与明文有关的默认值），作者对同一数据集（从2020年4月至2020年6月执行）进行了重复的实验：结果表明，有很大一部分app未充分使用该机制（如允许使用不安全的协议）。 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72Evkm1VibmdrgI0DaagtwHFWicxRTPEFqcnS1ZPriaw9RgsOFhn5jkaWc6ia7g/640?wx_fmt=png) 

  之后，作者探索了弱策略被采用的原因。作者发现，一方面是由于开发人员在设置过程中，许多策略是从流行的开发者网站（如StackOverflow）中复制粘贴过来的。另一方面，App中嵌入的广告库可能会引入弱策略。   
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8qtnWE0YXWlcfaRvO72EvkQR6cAXF8Hd2rlm4VpOyDiaBZyiaOmZ5HhVKJDDU07ic6oFNPaCO76IVbg/640?wx_fmt=png) 

  最后，作者设计并实现了对当前NSP的扩展，该扩展允许开发人员在“应用程序包”粒度级别上指定策略，能够嵌入广告库而无需削弱核心应用程序的策略。 

  论文PDF： 

  https://www.usenix.org/system/files/sec20-possemato.pdf 

