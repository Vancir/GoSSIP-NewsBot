 今天我们为大家介绍一篇在2020年新冠疫情背景下的一篇安全研究论文，一作是曾经在G.O.S.S.I.P完成毕业设计、目前在美国深造的温昊煌同学 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSoewZHOnZaS8ZqHOaQib281YxY2bmgH1X2oGJYaVPX4mCtgCbD2FyNIA/640?wx_fmt=png) 

  这篇论文研究了41款上关于用户行径追踪和新冠潜在感染关联的app（Android和iOS平台均有）中存在的隐私问题，众所周知，在人类过去的大流行病周期内，从未有过今天这样便利的条件，可以使用数字手段追踪每个人的行踪，并帮助流行病学调查。尽管各个国家政府都推出了一些contact tracing apps，但是这些app可能存在一些隐私风险（特别是开发者对安全缺乏重视的情况）。作者对41款app使用GPS和BLE的情况进行了调查，并反编译了这些app深入分析其中的逻辑，发现其中很多app的确存在隐私泄露的风险   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSz8bMyR6NhJ9e8RsrJSD9sC6pJnlkkPgpxJwhqtE5FTnSmBkKSfxBfg/640?wx_fmt=png) 

    
 

  由于移动平台上的app想要获得地理位置信息，均需要通过系统API，所以作者针对app的分析，首先通过对代码中特定API的分析 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSmyzzQYSARcyiayYNWicjzql3r4txSwu06XRQTbSiagPibQX5DeaccxASZQ/640?wx_fmt=png) 

    
 

  然后作者研究了app如何收集用户的私有数据，关注了一系列涉及到用户隐私数据的API   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSScxn5y6FPAKbicGR7ib9wNO1fvQmJ4OibTUtb9jt7kVJWR9EwtdtDHgRyQ/640?wx_fmt=png) 

    
 

  最后，作者还把app在不同平台上的情况进行了对比，如果一个app既有Android版本又有iOS版本，那么会比较一下两个版本的app在隐私策略上是否一致   
 

    
 

  作者对调研的app进行分析的结果如下 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSZ7WSrGkPMpMSYD8RVtgnULFw8cSGuNextC5RWnSx5pT46KSbS5rmoA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSxj3rbia2HhVo4kZwEdkfIXjYycteiaRYp5iaDdAxAHZPDiatSTFBmZyA1A/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSbXteBpSqBCYEeRJmKJw8IcCbpAEZjWbVqkW6a308fvibxAOujIuJBKA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSTOdYn6XSlZOKDoB18TsKPZFqJ9LkLWMy8jMAdibQGavxvaOwb4tIEkA/640?wx_fmt=png) 

  研究发现   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSd9GBbiaGNB9SmxkluMMBdVVBgyJNepibykaq5NSVUhwHa9277JUFPZwQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSDMCjkqZIdaibIBniaIAYu3ewSjNpFHLk43PxuSTmUN4t5FY5trPQd7xg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibzyg0EqNgymZMmlC6iaTibSSNwd1sVQxtsibkn7dJjZ0hk0kvam8GlwZ4XxjibIOfxk4AtSW56lB2h7Q/640?wx_fmt=png) 

    
 

  论文PDF： 

  http://web.cse.ohio-state.edu/~lin.3021/file/SECURECOMM20a.pdf 

