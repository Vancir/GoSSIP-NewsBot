 在程序分析领域，符号执行是一项非常重要的技术，今天我们来看一篇标题很吸引眼球的关于符号执行的研究论文，发表在ISSTA 2020：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgakQLt32icXv12lnGuVONicxd2XK05EwWeBun9rck58v00E8YvqLYiaSRcqA/640?wx_fmt=png) 

    
 

  作者针对符号执行经常遇到的资源消耗问题——在针对实际的应用程序分析执行时往往很快耗尽内存资源这一问题，提出了一种折中的解决方法，即遇到路径爆炸导致内存消耗殆尽时，将当前的执行中间状态保存在磁盘上，然后选择部分路径继续符号执行，这样可以让整个分析过程持续进行下去。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgaklWDEryO2iag6X1XGqQqo5c78O8UZ3HhQpof7TZzldIzywYYxW14o0Kw/640?wx_fmt=png) 

  下图给出了一个简单的实例：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgake03EiaVclOb3hjjmSOBwKxhpiczicoWjiaywm40cORRia3GoSLeHZzBfYZQ/640?wx_fmt=png) 

  针对执行过程中的不同状态，作者对不同的节点进行了分类，如果节点不再需要探索，可以将其从内存中移除并将中间状态保存至关系数据库中，把内存留给更需要深入探索的路径。   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgakoo3umCibROiahJricvXicrrKv1TGnoMSnFsg46pXwb0Ya6xt4GRYwmWjoA/640?wx_fmt=png) 

  事实上在2012年的ISSTA会议上，已经有研究人员提出了memoized symbolic execution的概念，但是该技术并不能处理大规模的现实应用程序，其中主要的问题是当执行被记录并重放时，一些环境状态可能已经改变并导致重放的执行会进入到无效路径，这种改变被作者称为divergences，作者的工作重心之一就是研究如何有效处理divergences，论文提出了一个divergence detection算法来处理： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgak9z1NO4oqsuyEGPubrcF9KwRfffofZgaPBl3JnC4n0dMIsrXH8fibXdg/640?wx_fmt=png) 

    
 

  作者将经典的KLEE符号执行引擎扩展为MoKlee，对GNU Coreutils进行了实验测试，实验表明，当使用了相关的剪枝优化策略之后，MoKlee能够大幅减少符号执行的开销 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgakhwf0Bicu8ynHWYgiausNd5ic1icLcXLmYFyBHibqX8Bq8Mk0YET8DsA94icg/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9nXOXiblYtgsIUWY3oPpgak4afpjWuwjt0qHNicCV5ZDdOAnsvNrKIpdxwrj3N9htQvwRSUV58UicKA/640?wx_fmt=png) 

  MoKlee的核心优势之一在持续符号执行时的低存储开销，这也是其对本文标题的呼应：可以持续地对程序进行符号执行探索。作者对那些因为内存限制而在常规符号执行时永远无法探索到更多路径的程序（从GNU Coreutils中选择的base64, basenc, cut, dirname, fmt, fold, head, mktemp, paste, realpath, stty, sum, tac 和 wc）进行了长达7天的测试，发现对单个程序最少只需0.6 GiB   
 (tac)，最多需要37.7 GiB (wc) 的存储开销，在现在硬盘比猪肉还便宜的情况下，完全可以接受！ 

    
 

  论文PDF： 

  https://srg.doc.ic.ac.uk/files/papers/moklee-issta-20.pdf 

    
 

  相关实验数据： 

  https://srg.doc.ic.ac.uk/projects/moklee/ 

