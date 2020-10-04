 今天给大家推荐的是来自USENIX Security 19的一篇关于Apple Wireless Direct Link（AWDL）的安全研究工作。 

  ![]() 

  AWDL是基于IEEE 802.11标准的专有无线ad hoc协议，其核心在于使用信道跳变（channel hopping）机制来实现与AP和不同信道上的其他AWDL节点的“同时”通信。这种信道跳变是由一系列所谓的Availability Windows（AW）实现的。对于每个AW，一个节点指示它是否可用于直接通信，并指示它将在哪个信道上。每个节点在AWDL特定的IEEE 802.11 Action Frames（AF）中定期宣布自己的序列，该序列由16个AW组成。AWDL节点选择一个公共主节点，并使用其AF作为时间参考来实现同步。每个主节点根据其本地时钟传输同步参数。 

  ![]() 

  AirDrop是允许iOS和macOS用户使用AWDL作为设备之间交换文件的方式的应用程序。作者通过使用MitM HTTPS代理以及在macOS的sharingd damon和Sharing框架（实现了AirDrop），对AirDrop协议进行了逆向。作者在Python中重新实现了AirDrop，并将其作为开源软件提供【https://github.com/seemoo-lab/opendrop】。其工作流程如下图所示。 

  ![]() 

  作者分析并发现了AWDL和AirDrop中的安全和隐私漏洞，在iOS上提出四种基于网络的攻击： 

  2.   长期的设备跟踪攻击，尽管进行了MAC随机化处理，但仍可能会泄露个人信息，例如设备所有者的姓名（超过75％的实验案例）。 

 
 4.   针对AWDL的选举机制的DoS攻击，从而使目标通道序列不同步，有效地防止了通信。 

 
 6.   中间人攻击可拦截和修改通过AirDrop传输的文件，从而有效植入恶意文件。 

 
 8.   对Wi-Fi驱动程序中的AWDL实现实施了两种DoS攻击。攻击可通过注入特制的帧来使附近的Apple设备崩溃。这些攻击可以针对单个受害者，也可以同时影响所有相邻设备。 

 
   作者的Dos攻击采用图9所示的方法进行去同步，从而最小化两个目标的信道序列重叠。通过ping程序测量数据包丢失，作者评估了去同步攻击的影响，如图11所示。 

  ![]()   
 

  ![]() 

  作者还根据Airdrop中存在的认证缺陷实现了中间人攻击，大致来说，就是 

  使用TCP重置攻击，将包括RST标志的TCP段发送到目标使其立即断开连接并有效地防止了从发送方到接收方的任何重新连接尝试，接着进行认证的降级（诱使使用者更改设置），最后进行转发和修改数据传输。 

  ![]() 

  在AWDL分析和构建AWDL原型期间，作者还发现了一些Kernel Panic和System Crash，并基于此进行DoS攻击，视频【 

  https://www.youtube.com/watch?v=M5D9NeKapUo&feature=youtu.be 

  】还是挺有趣的。   
 

    
 

  原文链接：https://www.usenix.org/system/files/sec19-stute.pdf 

