 今天我们推荐一篇已经被Usenix Security 2021会议录用的论文，利用ARM处理器的Pointer Authentication Code (PAC) 特性来对程序进行内存破坏的安全防护 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaDEtqdrJicIb6eiaWaFAQmMMETQK7DCC27tNnhiaSH837x8NUDqHNLriaaw/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaYib1MJDYEWGGnpo2DH0KiaNylmFB5NeNyv8Ckss5D6GmlglnJQWIRqIA/640?wx_fmt=png) 

  作者运用PAC机制，实现了名为PTAuth的系统，动态检测时序内存漏洞（在论文中特指 double free, use after free 以及 invalid free 漏洞）。其核心思想思想在于将内存对象与指向内存对象的指针通过某种特定的方式绑定起来，并在指针解引用时检测指针是否合法。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9ia5dquoKnEJgAwsH9DJH1ov9Cz7ow7SuzjMcpqgtpibtNPI7r0Czic0NxQ/640?wx_fmt=png) 

    
 

  针对动态分配的堆内存对象，PTAuth会根据对象的地址以及 object ID 通过运算生成 authentication code（AC），并将 AC 存放在指针的高16 bit 位置。一旦指针被释放，ID就会改变，因此在下一次使用某个被free的指针时，PTAuth会重新计算 AC 并将其与指针的高 16bit 做对比，如果两者不相等，就会报告问题，并终止程序运行。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaRprTxL9rqxv8oxQFbr82VJgehjn8mMzGEkpaeVoc9DBBKn24vvbicnQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaPE9libXtUOIQ11yp6VFxtNfRDSVLNico8ADzoSHYibHKOjXNlyXF9bUuw/640?wx_fmt=png) 

  PTAuth 针对 ptmalloc 分配器，对所有的堆创建函数 malloc/ calloc/ realloc 等函数都进行了修改。也就是对分配出来的对象前面加个 8 字节大小的 ID ，并且生成 AC，将其放入地址的高 16 bit 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaNyUUXMn4FficnsLaIcWv6uwzIUkXAtU7ZJaqzNHAxP0CtM0yKWfNFGQ/640?wx_fmt=png) 

    
 

    
 

  由于还没有办法用硬件进行测试（ARM还没发布支持PAC的硬件芯片），作者在模拟器上对 juliet测试集以及 SPEC CPU 2006进行了测试 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaLp00Sp33lJzxDb6ZP62qDW1EKCH3vXIMcUQvzvy3sM0d5dw93Qce5g/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iaQ49iaoIDlYK2dbgCQ0HhvDlZKl1X4O9QYjJFiaPE70sEo8tkUQZlSrqw/640?wx_fmt=png) 

    
 

  作者还比较了PTAuth和其它几款相关防护系统   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib14F3WJs0f0h2VJ0YE4w9iahhhZmiaFibFwjmjVyBwrDiad74823eoBNA0KDNa4wYXj7TiaCpYcmzFyNQ/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://arxiv.org/pdf/2002.07936.pdf 

