 冠军是衡量体育比赛参赛者的标尺，而针对技术问题，由于往往缺乏一些统一的标杆，让不同的工作之间的比较产生了“关公战秦琼”的状况，今天我们给大家推荐一篇技术报告，试图为fuzzing这个领域提供标准的“度量衡”   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjGheKKFlOm8Drg92JcWFjLEeML9rMYsiacJIe6wzT7EhvV8kBJKgkktQ/640?wx_fmt=png) 

    
 

  作者的研究目标非常明确，就是去建立一套评估不同fuzzer好坏的统一框架，作者设计了名为Magma的框架，使用现实世界中的代码，并插入了生产中常见的bug用于评估fuzzer，作者对六家不同的fuzzer（AFL,   
 AFLFast, AFL++, FairFuzz, MOpt-AFL, honggfuzz）进行了评估，评估结论是……且听后续分解 

    
 

  先来看看Magma的设计需求： 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjpWBY5davZ5sSJeN2vgpzt3v4TxAxcZLTr2FtWHwRjexFicDvdnPQg8w/640?wx_fmt=png) 

    
 

  Magma实现了一系列复杂的bug instrumentation，并利用libpng、libtiff等现实软件进行评估。   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjPKU595W1rvaFeibr1STUhUo5gXuVBQy3h3ibNUSlxrdQ49HH6GALxeicw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjEzV6OTtQBt7r4L8C0WoPEicWTaWGKzHeQgW7S4rEJFPROwpwRJ7VX8g/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjcqic3OciaeODCdsrSniatCpibxRYv4nu2VdpGah2iavQawlLDbER2Mu6taQ/640?wx_fmt=png) 

  接下来就是激动人心的 金球奖 最佳fuzzer 评选环节了：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpjWr5s2aIq6ibIe37mbrJcGn0abtVJ9OwBC4QZJx8FMicSWfUR45SXic8BA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpj1Q4QANQ7QmRorWUZf9btSkT4jms4bgYmeOj5AJ3x3SHR6PAicm7gWkg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od85kTHeqsKGsEKppX5YHLpj50pfAlvicAFxePGOeAr8SibOShDBwNygpHAwGYuic86x1rXtDe9G4krHQ/640?wx_fmt=png) 

  作者对测试进行了总结：首先，对于测试的六个fuzzer发现bug的能力，作者认为都差不多（尽管有些fuzzer在特定测试项目上表现突出，但这不能代表通用性）；而对于性能这项指标，冠军fuzzer是honggfuzz，性能非常好；作者还讨论了其它一些导致fuzzer运行比较挣扎的因素（例如magic value之类） 

    
 

  最后作者承诺会持续开发magma，让其变得更为自动化和全面化 

    
 

  论文PDF：   
 

  https://hexhive.epfl.ch/magma/docs/preprint.pdf 

