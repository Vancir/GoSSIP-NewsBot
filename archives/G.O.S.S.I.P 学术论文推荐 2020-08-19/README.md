 跟随昨天推荐的BLE安全研究论文，我们今天继续来看一篇关于蓝牙安全的研究论文，只不过这次作者关注的是蓝牙中的密码随机性安全问题：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48BvqvwHoicnAqPpQDdzSVB0t93YwhY8cNPJBCddYvLz3jw3qrR6RsrSJ2A/640?wx_fmt=png) 

  作者研究了蓝牙芯片（主要是Broadcom和Cypress这两家厂商的芯片，用在三星S8和iPhone上）中的随机数发生器，研究发现，尽管芯片上均自带了硬件随机数发生器（HRNG），但是作为备份措施，系统也提供了一个软件伪随机数发生器（PRNG）作为第二选择，然而这第二选择的熵（entropy）并不优良——由于可预测输入的原因，软件PRNG容易遭到攻击。不过作者的研究都针对的是已经发布一段时间的芯片，在2020年以后的产品基本不存在这些问题了。 

    
 

  在BLE的协议安全设计中，很多地方依赖于随机数的可靠性，如果随机数可以被预测，则攻击者大有可为，例如经典的基于六位digit code的蓝牙配对，其中的协议就需要随机数来支持ECDH密钥交换，如果随机性遭到破坏，会导致Numeric Comparison protocol attack 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48BvaWkQFzYCWmFZXEjQd5ozmKsDibRyvx2ljiaFgpD0yxg2YpibPh1O2ia3SQ/640?wx_fmt=png) 

    
 

  作者逆向分析了一大堆包含Broadcom和Cypress蓝牙芯片的硬件，并对其中的HRNG进行了黑盒随机性测试，也分析了作为fallback的PRNG的安全性   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48Bv9M7PtGBpcykVicWsCEhicca9ibPamI4ejwYW4ibPaY6s4lQ0Os6wygzalA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48Bvwl2dngFL9sSEiaQAsEqdllB9Y9Ge48GOXBq0bOf2dgTMlic7v6tKXVWA/640?wx_fmt=png) 

    
 

  作者发现，各种设备中的PRNG实现各有不同，有的完全没有任何安全性（zero entropy），而作者主要关注了其中Variant 2 PRNG的问题——该PRNG中使用CRC32作为压缩函数，由于CRC32是一个仿射函数（affine function），当攻击者得到该PRNG的两个不同的输出（a和b）时，根据公式：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48BvHaWibSWxwGxoYFcxzZiacZTb4paRico2meNJZMgneo7oxTRucicbzMwzOQ/640?wx_fmt=png) 

  攻击者只需去寻找暴力搜索a和b的差分就可以开展攻击 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48BvpUl8mibHib0uiautZ6kWcMI4l3f4puBwaiaMNMRVd0RREx7drmibxBVh9VA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibe4DM0ECrMXGHe40FZ48Bvia61GLEPURXLSZp5v8yDlxZa1GFsLHrztJqBC3vXDJU9qmzFKrKqqQw/640?wx_fmt=png) 

    
 

    
 

    
 

  论文PDF： 

  https://www.usenix.org/system/files/woot20-paper-tillmanns.pdf   
 

    
 

  演讲slides：   
 

  https://www.usenix.org/system/files/woot20-paper24-slides-classen.pdf 

    
 

  作者开展研究用到的一些工具集（internalBlue，听上去好像是永恒之蓝……）：   
 

  https://github.com/seemoo-lab/internalblue 

