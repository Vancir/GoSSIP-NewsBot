 容器安全是近几年大家关注的热点，今天我们给大家介绍一篇RAID 2020会议上关于Docker容器安全的研究论文   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYh3QBlhRZwKrePPCq4ldW35PIjFEC1NHI0S2ADSHXwmChFhwx9sGXz2A/640?wx_fmt=png) 

    
 

  容器和虚拟化技术的一个本质差别在于，针对容器的安全隔离是基于操作系统内核实现的，而容器内部往往会利用内核的漏洞发起提权攻击，然后破坏隔离穿越安全边界。为了减少攻击面，常见的针对容器的安全防护措施之一就是减少容器可调用的syscalls，然而这需要对不同的容器中代码进行分析 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYhOz3AorcYVM5z0d7XtsJ2om0h3wqj2QEg9Hia3lkUredWibxazlgXw9aQ/640?wx_fmt=png) 

    
 

  然而针对容器中的代码进行分析，不管采用静态分析还是动态分析，传统方法均有弊端，例如上图展示的动态分析方法往往会漏过一些控制流，而静态分析则比较保守，让许多不该调用的syscalls被放行。作者在本文中设计了Confine系统，特色在于首先用动态分析追踪标记了所有涉及的可执行代码，然后再用静态分析尽可能全面地检查，并过滤掉该容器镜像不需要的syscalls 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYhSQ1aUxeIn9aj6nIncVicg4MbWibrhibfJUGGA5LwxB3GdwDyj0ibgiaTBsw/640?wx_fmt=png) 

    
 

  作者对常见的容器镜像进行了调研： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYh7nglgnn4C60FeaCo5NrqEv2ib6qmEb43PtVe7AvPxqIQZJ3C6kwuRYg/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYhHsjvDichF8eibwUffaU8mufZs7zJsQmG1uYAHR5JkZck47SYBpCLZuibw/640?wx_fmt=png) 

    
 

  然后作者对150个容器镜像进行了分析，其中大约一半的容器镜像被Confine屏蔽了至少145个system calls，即使是最差情况下，Confine也屏蔽了100个以上的system calls，而Docker默认的default Seccomp filter只过滤了49个system calls。通过过滤这些syscalls，如下一些漏洞攻击不再可行 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odicRHmv8DkfwSWtD969TibbYh9Q6e1DRPWqfJ5zskibribeTicu3QjDxZmyQVmb68xmGfeezzchicAAWibTQ/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www3.cs.stonybrook.edu/~sghavamnia/papers/confine.raid20.pdf 

    
 

  项目主页：   
 

  https://github.com/shamedgh/confine 

