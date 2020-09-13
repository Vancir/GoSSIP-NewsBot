 我们今天为大家推荐的是一篇在Usenix Security 2020会议上荣获Distinguished Paper Award的研究论文 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCf0ibjSjZ8pEeQaiauynWRzuh0LSLHgkt9paqSuicApWs7VVzyR23iatfib3Q/640?wx_fmt=png) 

  作者在本文中引入了Datalog（https://en.wikipedia.org/wiki/Datalog）这种程序设计语言对反汇编工作进行增强，Datalog和Prolog语言类似，是一种声明式编程语言（declarative logic programming language，常见的四大类编程范式之一，其它三种为命令式、面向对象、函数式）。这种语言虽然不常见，但是特别适合逻辑推理，可以将一个Datalog程序想象为一组rules，通过这组rules进行推理就可以得到一些结论。我们经常玩的数独游戏就类似这样的一种逻辑推理过程，实际上，我们发现确实有人用PostgreSQL（SQL条件查询和基于Datalog推理是一样的原理）写了个soduku solver (http://conway.rutgers.edu/~ccshan/wiki/blog/posts/Sudoku\_in\_SQL/) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfUX16pxfgenmKKl3JI71ldHZiakr6fNokCUjJd0zGKrImmsFq5jjBVDQ/640?wx_fmt=png) 

  回到论文本身，作者认为，反汇编（x86代码）中两个核心问题——判定一条指令的开始和结尾，以及判定一条指令中的操作数是地址还是数值，都可以归结为逻辑推理问题，因而可以用Datalog辅助解决。实际上就是将反汇编过程中的一部分静态分析工作交给了Datalog来做。   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCf4tic93EiaDkibXrUjZ2PHNnMzuGnXGUia7FibP86HWG2nqG6UyPLHxUT3icg/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfPkmaYWsdTOHIt7uMW8xPFQQM4McdH25eWhoxgBCE24tSQz4yTaBVJQ/640?wx_fmt=png) 

    
 

  作者首先将程序反汇编的初步结果（使用Capstone从地址头部开始，每个字节尝试一下反汇编）转成Datalog规则，然后就让Datalog去做推理，把不符合事实的去掉，留下的就认为是正确的结果（这个过程很复杂，大家可以去尝试理解一下Datalog……） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfSwoFZ92oSq5Ejb57G0tZ7SGHOMBBbCn3RcyMIoiaOoQ7B6kr4miboXnw/640?wx_fmt=png) 

    
 

  作者研发了名为Ddisasm的工具，并将其与Ramblr（Ruoyu Wang 和 Yan Shoshitaishvili 等在NDSS 2017上的论文Ramblr: Making reassem-bly great again）进行了比较： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfLpFRiawI8N9fFCLFp8Oc5KIGl61SniaKTETXptrfpOMMev9H1BnrjZtA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfjTuicAbzxRa4V3bDliajNRec4ia9xQcmUiavcKTQbabYTsjnic8zxsw77qA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfgoZcXGg8HHlOlv5Zv9wTZnKuAibRP7ArtV0U80PhaibxibUJqhQgh1EEg/640?wx_fmt=png) 

    
 

    
 

  作者还附送了一个基于他们公司（GrammaTech）设计的中间语言GTIRB（GrammaTech Intermediate Representation for Binaries）和Ddisasm一起做二进制代码重写的教程： 

  https://grammatech.github.io/gtirb/md\_stack-stamp.html 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibaR1UF77AuibLv4ecrcCQCfmaFQPR4YqtxfzJSQzRATh71vTBlPCEApFoW8k6pzG0micbWeibzbLsFQ/640?wx_fmt=png) 

    
 

  ---- 

  论文PDF： 

  https://www.usenix.org/system/files/sec20-flores-montoya.pdf 

    
 

  论文slides：   
 

    
 

  论文开源项目： 

  https://github.com/GrammaTech/ddisasm 

