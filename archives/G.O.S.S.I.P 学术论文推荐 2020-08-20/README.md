 今天我们推荐的论文是来自USENIX ATC 2020会议上一篇关于容器安全的研究论文   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFibEmK23ibUW9jV53gJ1S3GKsFNnrW3VyW27056813DLnypV6aMluDmqA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFotS3SILjop8B89bLseZ7S042dlAs8wRJrXCO4URNbFaicr86MBqP79Q/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFz3sFZPZs6IRVib80mqYGvQIfBRVe8WHZfafiaibcmfHWibFza63tyhTzAA/640?wx_fmt=png) 

  作者研究了Container Networks即多个容器组网形成的结构中的安全问题，作者指出当前的容器网络管理通常基于操作系统本身的IP级别访问控制（通过iptables来实现），这种访问控制机制存在五大挑战，如下图所示： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFVuZkQP40icfcSmV57xB4Fqqd7zic9l6tKOuhDewkX4ibBwiaIycXiaicqyJg/640?wx_fmt=png) 

  为了解决这些挑战，作者设计了名为BASTION的高性能安全网络栈（high-performance security enforcement network stack），通过BASTION可以抵御多种以前的安全防护机制抵御不了的攻击   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFWL4Icpza4HJSiaP7QEGmmFjN9KE1JCgqkESaRoicibnET2aoiaAiaCcJaxA/640?wx_fmt=png) 

    
 

  BASTION的核心包括一个记录了所有container之间安全依赖关系的manager，以及network visibility service和traffic visibility service；其中network visibility service负责对容器之间的通讯进行安全审查，而traffic visibility service则负责执行容器之间的安全包转发 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuF4tfc270BYvBMVuxmRZ9sAYmGOSk17pxYkjyYbHE8FNEc4NPsrHOhaQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFMAply1ibazmYLWm1HYZbz8fhw21N30XcYqTFwtzibNKHaaMGdNiblnJSw/640?wx_fmt=png) 

    
 

  在保证了安全的同时，BASTION具备很好的性能，不会让容器网络通讯变得更慢： 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFwXNzn62yaNwnNeIoePb4GuwNgt6DfDkWRrv5bPBszDmLYnoACkH1hA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFtJGPlLleicOoaWYg0hzqibzkjVVyYhDCgbkLXfib7hYSrrslh7Ee0pRKw/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odib9ylr2dlcpYrThgyvkCfuFiaIyUatghb3cJ4FSBNzkdZYhLxicfYhJTTLoibgBGgTqtFB5ZBunsolKg/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www.usenix.org/system/files/atc20-nam.pdf 

