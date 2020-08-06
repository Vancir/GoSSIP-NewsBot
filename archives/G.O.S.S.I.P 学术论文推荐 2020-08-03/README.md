 8月份第一期论文推荐，为大家带来的是Eurecom的安全研究人员发表在Usenix Security 2020上的研究论文   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOph0edWXRiaY3mFO37ick3URZaNg6q9TeVcgKFtsYEA7roO5LdNRPNCjjg/640?wx_fmt=png) 

    
 

  该论文聚焦符号执行的效率问题，指出传统的符号执行的效率低下主要问题在于其采用的解释执行（interpretation）策略，为了实现高速符号执行，作者设计了将符号执行代码和原始代码捆绑在一起执行的方法，并设计了一套基于LLVM的编译系统SymCC，可以直接将现有的代码编译生成出原生执行+符号执行的binary！   
 

    
 

  我们先来看看传统符号执行的方式：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOpCncF8UQ2csUVP7cpKPb7yibpFvKoeiaGxpviaI1ONk13kgmseNjAkCxrg/640?wx_fmt=png) 

    
 

  通常情况下，符号执行会采用基于中间表达形式（IR）的实现，例如著名的KLEE系统   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOp1fvPX0GAfpmTUV24c3neW0kZFgaOFU4NpsJkibia4ZH4rvIUq4xIibBNQ/640?wx_fmt=png) 

  考虑到性能，一些符号执行引擎会直接插桩binary code（利用PIN插桩框架等）来提升效率   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOpibjBibnkIpmvGLU3lh5IOwiaL2lvY2uoiaaO3IsLMwUpiaEqwk58uYkvggQ/640?wx_fmt=png) 

  作者提出的SymCC直接在编译期就开始在生成的IR上植入符号执行相关代码，进一步提升性能   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOpDwFSZbVxedAAbOoSwiblBQGCd9UhVeBcb2sic5Q29Pfxkum2LOjdMUAQ/640?wx_fmt=png) 

  看看性能对比：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9UCDib4WiaEzLicKw19S8NeOpHv3VricTAiafpiamXCxC23CDfXicguZet2ElxsicqxyuXz3wCLORfFtPBQw/640?wx_fmt=png) 

    
 

    
 

  论文PDF： 

  http://s3.eurecom.fr/docs/usenixsec20\_symcc.pdf 

    
 

  项目代码： 

  http://www.s3.eurecom.fr/tools/symbolic\_execution/symcc.html 

