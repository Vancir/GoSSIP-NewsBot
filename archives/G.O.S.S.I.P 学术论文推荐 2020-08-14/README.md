 又到周末啦，今天给大家介绍一篇来自TDSC学术期刊的Android恶意代码研究论文   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxsxtUlnRzdpZYBkbfkpKq0icC1CCNIrhVpoobibKYCLII1BrPnrmbbsvKA/640?wx_fmt=png) 

    
 

  在2012年IEEE S&P会议上，蒋旭宪教授和周亚金博士发表了著名的论文 Dissecting Android Malware: Characterization and Evolution （https://yajin.org/papers/oakland12\_sok.pdf），获得了超高的引用量。八年的时间过去了，本文针对malicious payload (rider) 在Android生态中的情况再次展开了调查（注意论文的研究时间不是到2020年，而是从2010年到2017年）。 ** 值得注意的是，G.O.S.S.I.P在2014年AsiaCCS上就发表了一篇关于malicious payload (rider) 自动化切除的研究工作（APKLancet https://loccs.sjtu.edu.cn/~romangol/publications/asiaccs14.pdf），而本文研究表明， ** malicious payload (rider) ** 长期存在，因此我们的自动化切除技术也十分必要！ ** 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxseUn7fyUFyBbSiaH944n2KSoGIJhmJQLmIZZqVaH2sO2rOfQD17gnNAw/640?wx_fmt=png) 

    
 

  作者利用了AndroZoo上的570万个样本进行了分析，用VirusTotal进行恶意代码扫描，发现这其中来自Google Play的apps（73%）中，有超过14%包含恶意代码 

    
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxsFSncmMza7m5j9I41m8w5sat43fuJyhgE0SQ3FKQiaZUaV0T8yKXVNDg/640?wx_fmt=png) 

  为了实现大规模扫描分析，作者利用了许多之前研究工作的方法，即将代码转成更容易分析的数据结构，如上图所示。基于这个数据结构来做恶意代码分类 

    
 

    
 

  经过分析，作者给出了恶意代码的趋势变化图 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxseXUTZ7iaZwFge1kbXHWTSaRX57jCbBV6wQjNiac4gjHSEg7vZC7hjSwA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxsGGd4EhNOfgE2EAp3WWvAd3SHklicwlvd3RKgibwN44Y7FI7XqHm7OZUA/640?wx_fmt=png) 

    
 

  作者对这些恶意payload进行了流行度调查 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxs0mDx37tbwTicGJwx76ibSeqHVasicibKDF3QaW8eLia1cU60A5esDQ2fcyQ/640?wx_fmt=png) 

  作者还对恶意代码的保护手段进行了分析   
 

    
 

 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib6mWWOsxtQ9R4Ll0JN1bxsH3wNATROa2MHhjcKoia7hEJjXeq7uT7OMysm05z56gpWOw0sT8TIGmw/640?wx_fmt=png)    
 

    
 

    
 

  论文PDF： 

  https://seclab.bu.edu/papers/riders-tdsc2020.pdf 

    
 

  论文github项目：   
 

  https://github.com/gsuareztangil/adrmw-measurement 

