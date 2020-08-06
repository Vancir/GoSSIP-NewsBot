 今天我们去DSN 2020学术会议上看看一篇关于嵌入式安全测试的研究论文   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hbXIh3wfgWqOTAxiaoWTMUWcJib13YXHEOlrTml0JSpy0Yx2k1mZzOFibSfesXicJ08wg277xAtk97Q/640?wx_fmt=png) 

    
 

  作者对嵌入式系统的安全研究进行了剖析，指出其关键问题之一在于如何提供精确的系统模拟，从而帮助安全分析人员运行嵌入式固件并对其代码执行进行更为细粒度的追踪和分析。为了解决这个难点，作者设计了名为HardSnap的解决方案，针对嵌入式系统模拟执行，HardSnap把那些硬件特化的部分给仿真执行了，要么使用软件仿真，要么使用FPGA仿真，其目的都是让模拟执行能够处理硬件相关的部分。   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hbXIh3wfgWqOTAxiaoWTMUdtrJRyIU30RicCCa4GvBQDv9xzjTFe3r6eujdlMgzYKPAQfZePuohtQ/640?wx_fmt=png) 

    
 

  HardSnap的核心技术是在运行过程中进行多次快照（snapshot），通过记录运行时状态，减少测试所需要的重复执行的开销（例如和fuzzing对比，不需要每次重启到初始状态） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hbXIh3wfgWqOTAxiaoWTMU5mRfQucrItyWYvibTjnUqnUiaECqwCRV2p460vmXg3nrGQzN8AWs4Wkg/640?wx_fmt=png) 

    
 

  HardSnap的特色之一是利用了FPGA来辅助实现一部分仿真（但是FPGA开发成本不高吗？） 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hbXIh3wfgWqOTAxiaoWTMUTTSoMKDPpJnp43e87OaD3oVvJnyWpDgwBZAvmyCiaXibq9SwxfANPiayg/640?wx_fmt=png) 

    
 

    
 

  和其它一些方案相比，HardSnap的优势： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hbXIh3wfgWqOTAxiaoWTMUjdwVA2KPR2CwLCfsMKWzfzBbDmIictmUOmcLwrcBuvyw1m7BdWj6icZA/640?wx_fmt=png) 

    
 

  论文PDF：   
 

  http://s3.eurecom.fr/docs/dsn20\_corteggiani.pdf 

    
 

  项目开源代码： 

  https://github.com/hardsnap/ 

