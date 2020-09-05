 今天我们推荐一篇由中美研究机构（IBM研究院和字节跳动AI实验室）联合完成的恶意代码对抗研究论文，发表在DSN 2020会议上，在现在的背景下回顾当时的合作，真是感慨万千   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEGdoibOVuIjT4yUGypAzibNo5QTu0EibDGtbkHbK4JVL192McfuCF0QWJlQ/640?wx_fmt=png) 

    
 

  之前已经有一些研究论文针对恶意代码会检测运行环境这一特性加以利用，将正常的系统伪装成“沙盒”或“分析平台”，让恶意代码误以为自己处在被分析的状态下而不去执行恶意行为，从而规避恶意攻击。本文作者沿着该思路，提出了Scarecrow系统，该系统能将运行环境模拟成一个分析平台，而且能达到不可区分的状态，让恶意软件自动屏蔽自己的恶意行为。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEG2fhgibPMpmFPSiaR854MB2t5d46qaemvQHyWVYz4jKvF9TwCFRohmmww/640?wx_fmt=png) 

    
 Scarecrow系统首先调查了软件、硬件和网络层面上各种分析环境的特征，例如在文件层面上，一些虚拟环境（如VMware、Virtualbox）会给系统引入特定的驱动（如vmmouse.sys）或特定进程（如VboxTray）等，同时恶意代码会检测系统中执行的进程是否包含debugger、注册表键值是否包含了特定的内容；在硬件资源上，Scarecrow把自己伪装成“贫困户”，让系统看上去是1核、1G内存、50G硬盘（听上去是给云厂商打广告）；在网络层面，Scarecrow会将恶意软件请求的一些不存在的域名访问都返回同样的ip解析结果，欺骗恶意代码，让它们以为自己处在sandbox中 

    
 

  作者从Joe Security和MalGene分别搜集了13个和1054个可执行并检测运行环境的恶意代码样本进行评估，同时还运行了20个最流行的Windows工具软件进行对比。针对来自Joe Security的13个样本，Scarecrow可以让其中12个自我屏蔽；对于来自MalGene的样本，Scarecrow可以屏蔽其中的944 (89.56 %)个样本 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEGddseF3AXNMqRaCQ3eMEGic9ia8sLNIr5UoqQhbkooXZ5nm3J3yDUGyRw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEGibQPUCVhK94Td0YAvHYibd6fDIm1ib1iaxhhEgRLFiaHMnsvpm77dvzxUAg/640?wx_fmt=png) 

  作者还仔细研究了恶意软件针对哪些项目进行检测   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEGjYqTbCvybLWopm7hd4hphjoxHjHQ32IHiaERKqial7ge1HRXzqibPCRJA/640?wx_fmt=png) 

  最后作者对比了一下自己的系统和一些类似的系统在高层面上的区别   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicsY38KdSTvL8Ny9Wpm5fEGq9AUh0hPIFF1PwictZFiamOV265HZftJiapfgawicGsicxGBhnRuqia9ibZJg/640?wx_fmt=png) 

    
 

