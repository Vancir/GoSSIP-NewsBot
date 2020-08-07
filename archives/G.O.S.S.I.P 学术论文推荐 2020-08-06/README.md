 为了保证学术论文推荐的数据方便访问，我们在github上(每日论文推荐https://github.com/GoSSIP-SJTU/dailyPaper) 共享了论文推荐的html（单文件版本）和论文PDF，请大家不吝啬你们的star！ 

    
 

  今天我们给大家推荐的是Usenix ATC 2020上的一篇关于低功耗蓝牙（BLE）的fuzz研究论文 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGibSDXqDkc9CuE87xDicDsCricxY5zB4B2lcZZqib5C3ejm2EOzu7usmIog/640?wx_fmt=png) 

  作者为了测试BLE的安全，开发了一套系统化的fuzzing framework，对蓝牙设备进行测试，支持在错误的时间发送正确格式的packet，在正确的时间发送错误格式的packet，以及在错误时间发送错误的packet（绕口令……）等等，通过该框架，作者发现了一类错误，统称为SweynTooth vulnerabilities 

    
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGl85RwXBgezyZJZpPiaiatoiaFLvsGt7P2CtxPtjS318NUliavaXw5xgvicQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGoI59icR7et0Pdttmp8CBhtPdFJzWtk0fVhuj8QO5x6JQgO97qHBkQlw/640?wx_fmt=png) 

  低功耗蓝牙在近年来一直被各种安全研究针对，其主要问题在于设计上对使用BLE的设备欠缺考虑，例如低功耗设备通常没有什么输入装置，如何让两个没有输入装置的设备进行蓝牙连接还能安全认证？ 

    
 

  另一类问题是蓝牙的协议栈软件实现往往存在各种经典的漏洞（如内存破坏），可以被攻击者利用 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGu7g4AiaAiaBvV0kUwLn93j0wzHxD2P4ntClxEbjicNHYolrvkV0tct5fQ/640?wx_fmt=png) 

    
 

  作者于是研发了针对BLE的fuzzing流程，如下图所示：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGenNFqic205AKpA5aWR5cqdDA5xFibSLJZZwbEKacmbfTNAdmN7jEzfhA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGw9p3rIUjX7IH1UibZlVNRwpKCg7S5PUC2mu2SKn8BLXzkibib62O0KEew/640?wx_fmt=png) 

    
 

  作者对常用的一些开发板进行了测试： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGfFvHLicATCocVwIdRRibLIMJ8ZlHichsEJeYSmg4xm7cUQ4Iut28Kwsicg/640?wx_fmt=png) 

    
 

  找到了很多问题： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGfxGctRD9Snic4lfEg2ll4GN5LjVsgAxsib0soaicqnY0bdxvwYvtfNKhQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGq6RaaibTt6V1zeWFJiccV3E4tQMQUWial8BjPPDugibKTu5Ysc2EYGshQA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib3efjibia7tryd3b0ialWdVvGBNJVDx4wu0OCcu6CcPz2lJpALz4oPNy7BtNQ63dKukHxkz6b4lkfIQ/640?wx_fmt=png) 

    
 

  然而作者在论文里面对SweynTooth这个漏洞的定义非常模糊，查找全文也没有办法找到SweynTooth的定义……但是作者建立了一个github repo并详细解释了相关问题： 

  * SweynTooth captures a family of 12 vulnerabilities (more under non-disclosure) across different Bluetooth Low Energy (BLE) software development kits (SDKs) of six major system-on-a-chip (SoC) vendors. The vulnerabilities expose flaws in specific BLE SoC implementations that allow an attacker in radio range to trigger deadlocks, crashes and buffer overflows or completely bypass security depending on the circumstances. (Update) We have also included a testing script to check devices against the BLE KNOB variant .   
 * 

  * * 

    
 

  https://github.com/Matheus-Garbelini/sweyntooth\_bluetooth\_low\_energy\_attacks 

    
 

  论文PDF：   
 

  https://www.usenix.org/system/files/atc20-garbelini.pdf 

