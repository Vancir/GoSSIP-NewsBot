 今天我们为大家介绍的是Usenix Security 2020上一篇关于通过减少攻击面来降低安全风险的研究论文： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3mgkoCajUeibnHx9IbucyKmOrNA4Ognt3CIOwoLWclv8cm3Qbl3brmgA/640?wx_fmt=png) 

    
 

  作者将研究目标集中在如何限定system call的使用上，提出了一种名为temporal specialization的技术，该技术将程序执行分为不同的phase，在每个phase有对应的system call黑白名单限定。temporal specialization技术建立在复杂的静态程序分析基础上，作者使用了大量程序分析技术来确定每个phase中使用的system call的范围，这种分阶段的system call使用管理，可以比传统的library debloating技术减少更多的非必要system call使用，从而降低安全风险 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry30yeicibqEUMgvIQ1K2fbN97TuYqHLwicGBspia1libySdIRuYNEaITn4r1w/640?wx_fmt=png) 

    
 

  作者指出，temporal specialization技术的核心是建立精确的call graph，作者根据下图的流程来获得每个phase准确的call graph，首先使用SVF这个框架进行指针分析，得到不精确的call graph（通常是过度估计），然后进行call graph pruning，具体包括两类pruning：Pruning Based on Argument Types和Pruning Based on Taken Addresses，最后生成seccomp filter 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry36RWibh87iae507u4O0ic7GApqc4IzWbkjtGuAPaHfSJQgz8rbkUyKTmtw/640?wx_fmt=png) 

    
 

  通过两类pruning，temporal specialization技术可以将call graph精确化，这样就方便生成一个更严格的filter，过滤更多不必要的system calls 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3mHpwOjTIGb50oZYG8LmS6kRbMsY9Bj2juRHEbvgOavNH8dgw9rLHoA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3icjYrcXh6Rlhy3Z9UGZW7RHZORL9OZcvWLb6DOqpMhArZ3Xypn3iaZtQ/640?wx_fmt=png) 

    
 

  作者实验表明，purning对call graph的限定还是很有效果的： 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3QnO5e9uhH54icFSebiaVGur976RGqUwicEFOubbcJvJUIRibzkzWNqZqFQ/640?wx_fmt=png) 

  同传统的比较保守的过滤相比，temporal specialization技术明显可以过滤更多的system calls 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3icwXtJyon4Ye9lib6nvCFjuPwe6NQYxrZXicVJoVxlgicc2KGkUzsiaPic5g/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3usiaWP1nWD7fIibGfvehibZvPprGTulTQayjJLpxYZ8O4Giav4lsJGiaibag/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od95XsVj0vU4xpxH9KWicyry3FGPEC8iapRnSiaoyReRkDawy9umaxSEImYHAWyZ8uhfbW8hDuIxjoI2w/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www3.cs.stonybrook.edu/~mikepo/papers/temporal.sec20.pdf 

    
 

  项目开源代码： 

  https://github.com/shamedgh/temporal-specialization 

