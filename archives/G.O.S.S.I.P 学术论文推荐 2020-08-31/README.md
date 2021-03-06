 8月的最后一期论文推荐，我们带大家去看一篇Usenix ATC 2020上关于Linux内核代码修复研究的论文 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVG7ydPibVmrQemDk9cicqMcyC0D5oiau1jeFB9QQa2JgaT0BgL07AdEuFkQ/640?wx_fmt=png) 

    
 

  在大型软件系统，例如Linux内核中，由于新的设计与需求，开发人员经常需要进行跨越多个源文件的大规模代码修改。 本文提出了一种从示例修改中自动化提取修改规则，从而帮助开发人员完成这些修改的解决方案。 该方案还可以进一步帮助开发人员理解现有的大规模代码修改。 作者基于该方案实现了Spinfer，并在Linux内核中真实存在的大规模代码修改上对其进行了评估。 该框架最终取得了86%的精确率和69%的召回率 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVG6m7iaK33HibfKCD5JOpZ3lib1og9HOcFU5pTUVGwIT4Moeqp3MAYr4VkQ/640?wx_fmt=png) 

    
 

  Spinfer可以从一些用C语言编写的示例修改中自动化提取Coccinelle semantic patch。该框架通过分析这些修改中存在的相似代码片段与控制流来识别修改模板并生成修改规则，其生成的semantic patch可以被开发人员直接用来进行新的大规模代码修改。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVGc2RLuicicGQ4Oxfa4CtJIrDl3n9GCAJxibWJPXVm04hwXQHpiamJ1sjjTw/640?wx_fmt=png) 

    
 

    
 

  作者在Linux内核中真实存在的40处代码修改上对其进行了评估。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVGLqYwjyDibHDW851d1Xibb64AeaaUdJyDbgRlJ3DGGBvxia3JtIOBWgrLg/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVGO3KG65XVKy7p5JOzPSbXiaoZlmhIsH86bBUBmc6ovGVZ5rGLghxSGqA/640?wx_fmt=png) 

    
 

  此外，本文还总结分类了在自动化提取修改规则的过程中需要解决的一些挑战，例如控制流与数据流的复杂性、代码修改的多变性。这些挑战也可以在一定程度上被用来作为未来相似工作的设计指南。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PiasdIn7BeydAk6AQkNWVGibfZ7HFIQrm2xdEHPQqvEd1RZI1HXh5RaXc3uJRMG1l5ibhy4oecevlg/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www.usenix.org/system/files/atc20-serrano.pdf 

    
 

  Slides： 

  https://www.usenix.org/system/files/atc20-paper578-slides-serrano.pdf 

    
 

  项目源代码： 

  https://gitlab.inria.fr/spinfer/spinfer 

