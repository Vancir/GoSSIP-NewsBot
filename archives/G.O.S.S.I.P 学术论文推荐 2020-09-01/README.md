 九月第一篇论文推荐，我们带大家看一下AsiaCCS 2020上的一篇来自牛津大学研究人员的关于污点分析（taint analysis）的研究论文   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldz05XRtHQvITiaCWCZaf8kwbBRONaBd8azt7vBX1icgegTNxbFtemrkzg/640?wx_fmt=png) 

    
 

  文章从改善污点分析的性能出发，考虑了利用just-in-time (JIT) 技术来帮助生成高性能的污点分析方法。作者研究发现，除了特定的污点分析引擎如LibDFT，一些通用的支持复杂污点传播的引擎如Dytan的性能开销都非常大（上百倍性能开销），要想跑得快，全靠引擎带，作者借助dynamic   
 binary instrumentation (DBI) 引擎的高性能作为基础，实现了污点兔子（Taint Rabbit）工具，能够以1.7x的性能开销实现复杂的污点分析应用（如exploit   
 detector, Use-After-Free debugger, fuzzer等等） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldqPNv0P3g4SCNjHz84CcAWicojI7FBJSyOnYQLPBYlFYS8UNUWtjbq6w/640?wx_fmt=png) 

  污点兔子利用了DBI引擎对二进制代码的JIT执行技术来进行优化，如上图所示，待污点分析的程序通过DBI引擎进行分析和生成新的instrumented code block的时候，taint policy也被集成进去，实现了通用的污点分析策略支持 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldTg95NROeu5xlUMC5v5HxuJ4EMeFo2jUSJEfc3PnziaD4OPSd8Y5z99Q/640?wx_fmt=png) 

    
 

  污点兔子的一个核心优化策略叫做dynamic fast path generation，但是作者对这段策略的描述写得晦涩难懂，建议大家看附录里面的示意图（Figure 10）   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldiaOOMPpUlhSpmrDmSxuqV1nVbqYaInQnHMzUQZlYLLPIgRg1g39PSDw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldkmGs0JKtG16vTBS4xSc96Chx5LiaqdAfFChne1c97HqJkhEIWWyfdbQ/640?wx_fmt=png) 

    
 

  污点兔子的主要卖点是性能，作者进行了详尽的性能评估，和许多污点分析引擎进行了对比   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldAjsCiaoL03g1aDkRSYFaB9R0wue69oDM42dV5ibXdUxOfiawx8U1DOw2w/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldUfm34hk7hib97HziagdJDoBBAv6HIBb6RCDpibtbxuqM3UXvo0VBqRYiag/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibXzD6T2hAGHhHPBSnHgGldzBg4kicQrfHksyxQnmP8xOt46LC0H5P7iavsibkHTZAH2zaBZD8uanjTw/640?wx_fmt=png) 

    
 

  论文PDF（预印本）： 

  https://arxiv.org/pdf/2007.05955.pdf 

    
 

  项目源码：（会议召开后才会开源）   
 

  https://github.com/Dynamic-Rabbits/Dynamic-Rabbits 

