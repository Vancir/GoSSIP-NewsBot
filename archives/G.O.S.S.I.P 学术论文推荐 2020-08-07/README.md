 周五晚可以追新的电视剧，也可以追一下2021年的IEEE S&P最新研究成果，今天我们的论文推荐就是来自2021 IEEE S&P的： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xPiapl4qibATK0e5CPeCN3vxMWfjNwdWN1POicZ5TL1dNYLgribViaPobCtg/640?wx_fmt=png) 

    
 

  论文关注网络钓鱼攻击（Phishing，此处应该cite一下作者之一的Ruoyu）的自动化检测，作者指出，在client side存在各种各样的规避检测的方法，统称为client-side cloaking，作者调查了112005个钓鱼网站，发现它们居然包含有1128种不同的cloaking手法，而且作者的实验（从2018年持续到2019年）发现，随着时间的推移，cloaking的使用已经逐步扩大化（从23.32%上升到33.7%），于是作者研发了一套名为CrawlPhish的检测框架，针对client side cloaking实现了精确的检测 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xbpQ6SrS66V6XpS7cH31KSgEyERDD7lwU2Efr1jbjwISWOwarTG7hUA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3x684r5XGkBUS8XrtOs01IPxiabDFB2Wua6lCX8ibUMkrr9iaibX9X5SwkeA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xtls7eZZ2oqErSoGhlQbYQsNPf43ZwEBCBOiaT2fFANkfaqfm4MprMWA/640?wx_fmt=png) 

  作者对client side的cloaking技术进行了全面总结之后，介绍了自己设计的CrawlPhish框架，可以强制执行网页上的逻辑，并移去一些妨碍分析的视觉效果 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xwhfsEEUXUGUEJLDkrNUcvHVXxFMEBAZHhtXF8KA8ZpRTMlOibhsSg0g/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3x5XPLQnJMs6buGW4g9A6dc1twueqhTRicqDASyiaPqtx9xYKmjw6maeKQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xsgLIl8A9CxwRysXI1BGj08aGk6hTd18thXBgiay0dQfkzXGhN8bxibUQ/640?wx_fmt=png) 

    
 

  检测效果：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xgPuxSrwoBtn4tpAvEELXHGMadU8WMKOZ2Qc26EJVAicegs0M1zBR1gQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xJNIqPDCdx6ibzbrbEQiaSuRAE082FrbW6ME88ibkcyRPAfsXa9KYZsh2A/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xh89wEiafj2agWIfaRjuLBSSP0GBFibbBiaTgP4jEibsYtQ1QxkRV6JjFzg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8u6cCWjGN84ZZ2dr0RNQ3xLdUeQU6QCkESIbBW6pplHTpODThwibB3ORygZ9epV5x5YpgLcI3yVZQ/640?wx_fmt=png) 

    
 

  这篇论文的结果非常丰富，实验做得相当扎实，展现了Oakland论文的风采！ 

    
 

  论文PDF： 

  https://haehyun.github.io/papers/crawlphish-oakland21.pdf 

