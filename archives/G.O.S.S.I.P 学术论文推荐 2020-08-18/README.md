 今天我们给大家介绍一篇RAID 2020会议上关于蓝牙安全防御的研究论文   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblw9ZpAhtUNr2UicFAGgqKiaZWI2tGeQiamNbFPZdFqjFOuoDZl39xB3UZA/640?wx_fmt=png) 

    
 

  近年来关于蓝牙特别是Bluetooth Low Energy（BLE）的安全研究大部分都是安全攻击类研究，而相关的防御技术比较缺乏，本文设计了一种检测虚假蓝牙信息传送（spoofing）的系统BlueShield，其核心思想基于如下事实：当攻击者发起spoofing attack时，必须首先广播包含BLE设备身份信息的advertising packets，这样用户设备才能发现攻击者的设备并被欺骗，因此BlueShield可以通过探测这类advertising packets，将攻击者和合法设备区分开 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblG4DXwC0nUupw9bOWxOOCTD0PXKwmljLpLaX2Tgr3Cvgv4iboSgzEIOQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblngia0BeBNX2ib2icV2SL6jQufjf6pibB94mgpv3GeRicFHOKZrYEEPVTkVw/640?wx_fmt=png) 

  BlueShield利用蓝牙数据包的一些物理特性和数据特性来对packet进行“身份鉴定”   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblbUOE2uibkDJNjrVFXttrsqs5UmDOFUOMgb7njKbicUPia1kywiacJkuBrA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblcBfMiabF5B1y3C5cF7NJIWc82k8P6ODkVQrGnmmDSXDcIOicsCiaWrTCw/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgibllJVoIgbo47NatVvth4DaLtk1SicFCj4eJh1c2XhXPVA5ibaeI2KuLvGw/640?wx_fmt=png) 

    
 

  作者用真实的BLE设备和树莓派、Ubertooth来进行了实验   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgiblamKfibTtyT01MN8NBrpkVeS1toApgtyUX51M1He5rPo4cKc7uym2Cyw/640?wx_fmt=png) 

    
 

  实验结果表明BlueShield的平均误报率是2.37%，平均漏报率是0.72% 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgibl2TNiaLxM2nRJiaIAEQQLU4uYd425x4cXrML6Gdz9wfGP14Eue1C5rQgA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicxe4iahZV7w6qQSIKEtUgibltiajiaNpT6AK87l3yzYdc7HoRfiakmJL3FLkH7OYQ8YYWFuNsRpLffBUA/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www.cs.purdue.edu/homes/dxu/pubs/RAID20-BlueShield.pdf 

