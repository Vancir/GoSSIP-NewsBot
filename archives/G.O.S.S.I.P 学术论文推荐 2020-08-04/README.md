 台风天正是读书天，今天我们为大家介绍卢康杰教授研究组发表在CCS 2020会议上的关于内核中过度处理错误导致安全问题的研究论文 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04L4eFZ05PwrZJd6mmdswuoBzzbiaibO6tVNSE6noUYoCr8MF5gUTU3Gp0Q/640?wx_fmt=png) 

    
 

  作者发现，Linux 操作系统内核里有很多的错误处理代码，如果过度处理错误，反而会影响安全性和可靠性，作者将这种问题命名为Exaggerated Error Handling（ EEH ）。EEH可能导致DoS、数据丢失、控制流完整性破坏、内存泄露等问题。 下图是一个EEH Bug的示例及其修复，这个例子里的BUG\_ON （Line4） 在传入参数为非0时，会让系统崩溃，从Patch代码（Line5-6）里看出，实际上异常处理并不需要让系统崩溃，简单返回错误码就足够了。 

    
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04LRFLIlYAZGmBhPJeewBw17JcFfIx6Zvbf9fp38bvjF8ibePRq3E67jUw/640?wx_fmt=png) 

    
 

  作者提出了一种检测EEH的方法——EECATCH。EECATCH以上下文感知的方式来检测EEH。作者实现了EECATCH的原型系统，通过跨过程、域敏感、上下文敏感的静态分析进行EEH的检测。实验评估表明，针对Linux Kernel，EECATCH总共报告了104个case，经过人工检查，确认了其中64个EEH Bug（ 48个已经被确 认 ） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04L82ic6CIovNicEEuiaIvL9iamqOt85uHFMaiaA12mQIic5fbkmzAEUy0XVWIg/640?wx_fmt=png) 

    
 

  作者通过grep linux内核的git commit，匹配关键词 reduce、remove、replace，以及下表中的Log functions和Terminating functions来定位目前已经被修补的EEH Bugs：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04LI08RpOev8R2Y5pFeianDGibghHJwWibAP9CuaLaPCadERqHztMia89cE7w/640?wx_fmt=png) 

    
 

  下表统计了EEH Bugs造成的影响：   
 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04LVeLsEbMdQ8xYrayYT2NicPR1kF9b72SOuIb3GUAnKYzDJKswxb5oTHw/640?wx_fmt=png) 

    
 

  EECATCH总共找到了228万个条件分支，62个新的Terminate Execution，112个新的用于输出Error Log的Error Handlers宏，收集了705个EH函数，13683个init函数，12891个exit函数。 最终找到的EEH Bugs分布如下表所示 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibpVWokl6RxUndncq0TZ04LliczfT1CU6mPLIuCXWic3ibkgFpDgXNywjQE3wHerYrNcpMogx9uKV5VQ/640?wx_fmt=png) 

    
 

  PDF: 

  https://www-users.cs.umn.edu/~kjlu/papers/eecatch.pdf 

