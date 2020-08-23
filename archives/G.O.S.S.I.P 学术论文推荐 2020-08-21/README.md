 周五的论文推荐，带大家去看一篇USENIX ATC 2020会议上关于Fuzzer与Sanitizer结合的研究论文 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvKK8Q2A1YyD6YwX1icBrKAXGJf6rt1sCkjGLyrqmmpM7h2OhZmiafKMYA/640?wx_fmt=png) 

  Fuzzer与Sanitizer结合是发现内存破坏漏洞的有效方式，但作者发现，在使用Address Sanitizer（ASan）对程序进行fuzz时，其中一个主要开销是内存管理（Memory management） 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvXdaLnHFwWTYL0FBvXuyhiavFb4vhjGb6cvN7My64wGb7WWMBJw5578g/640?wx_fmt=png) 

  作者发现，Memory management占用了ASan 40.16%的时间，作者进一步分析发现开销主要在以下四个函数： 

  *   unmap\_vmas (24.6%) 

 
 *   free\_pgtable (4.7%) 

 
 *   do\_wp\_page (8.2%) 

 
 *   sys\_mmap (2.6%) 

 
   由于ASan使用fork server的方式，提前构造好初始状态以降低开销，随后fork接受输入，子进程结束时需要使用unmap\_vmas、free\_pgtable释放内存。因为ASan需要使用较多的shadow memory，且copy-on-write机制的存在，fuzz子进程时会写入、创建shadow memory，造成需要使用更多的物理内存。而ASan在unmap\_vmas、free\_pgtable函数的开销就与子进程使用的物理内存数量有关 

    
 

  作者为了降低子进程结束时释放内存的开销，设计出了FuZZan。FuZZan在ASan基础之上使用了两种方式来实现shadow memory：红黑树的shadow memory实现以及min-shadow memory。且FuZZan使用动态profiling的方式，收集运行时的内存访问信息，以选择使用何种方式实现的shadow memory。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvCv2ib5pPa6KQiczNricibYiaia8ibgvtfFUVjTt0iad4E5Y7Zg2dNqda54G4Cw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvBPjHr5XrmQprTgtB1ZnlzXoaBSMiaj5KWTDGl0RVntS2Za2L3hdFE2w/640?wx_fmt=png) 

  Customized RB-Tree
-------------------

  红黑树的实现方式可以有效的控制shadow memory的内存开销，释放时清理所需要的时间较少，但增删查改所需要的时间较高。 

  作者认为红黑树实现shadow memory的优势： 

  *   low total memory overhead (leading to low startup/teardown overhead) 

 
 *   removal of poisoning/un-poisoning page faults (as each RB-tree node compactly stores the redzone addresses and these nodes are grouped together in memory) 

 
 *   a faster range search than shadow memory for operations such as memcpy。ASan对于memcpy需要逐字节比较 

 
   RB-Tree存储shadow memory适用于内存访问较少的场景。 

  Min-shadow memory
------------------

  作者认为限制程序能够访问的虚拟地址空间，能够降低所需shadow memory的大小。因此作者对原版的shadow memory进行了改进（各个段的大小、位置进行了调整），使得64位程序能够在48-bit address space to run in a 32-bit address space window(1GB for the stack, 1GB for the heap, and 2GB for the BSS, data, and text sections combined). 而不需要修改代码。   
 Heap可以根据需要进行调整1GB, 4GB, 8GB or 16GB 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvfJ96pibPQX1fqIrQsib1XFVXncOh6GC986vI5qAa82FTbzqZbG85Y4vw/640?wx_fmt=png) 

    
 

  作者使用动态采样的方式，记录shadow memory访问、删除、添加的数量，以及内存的使用数量。以决定使用何种方式来存储shadow memory的metadata。并会定期的(e.g., every 1,000 executions)、有条件的(e.g., when the fuzzer starts mutating a new test case)进行采样，以适应当前输入对程序行为的影响。 

  其次，作者对原版ASan进行了其他部分的修改。Removing unnecessary initialization、Removing unnecessary logging，以进一步降低开销。 

    
 

  实验部分，作者在Juliet测试集上进行了有效性测试：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvP2oSYicES7Rgr3KLl3GaIqxLnsxryozcBrOgibd4MExl093XIibl50g1g/640?wx_fmt=png) 

    
 

  而性能优势是FuZZan的主打：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvPcBsJtAHQa263LBYzxc3vsJ6aicPGRKJcNic5L8HPHuNcXZMV1QPP4ww/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvZonOvxk5diaKZad6WqAT4zG7N1FbyNqeELklrFz33Nnh7KgpTiaxa3aA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7PhcvTVSoXsvqOsJFxsDRtsurLibekJ0PVJJGGHKN1YBN3APmvBDia1GvbkWQ/640?wx_fmt=png) 

    
 

  在寻找bug的有效性方面，FuZZan比ASan更快： 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibYLexjNqnwk2zrtLr7Phcv2ibf95iasl77hcGVEEcNGn96GvztgEquCPVNEZuJ6t4YWjNBCpYv4yLA/640?wx_fmt=png) 

    
 

  总结：   
 

  原版ASan采用的shadow memory设计，使用空间换时间，而对于fuzzing而言，有部分输入的执行路径可能很短，使得大量shadow memory需要清理，此时空间换时间的策略并不划算。 

    
 

  本文的亮点在于，使用profiling的方式，根据程序访问内存的次数，以决定是用较少的内存（红黑树，程序结束时清理内存开销较低），还是较少的访问时间（min-shadow memory），获得了很好的性能-效果平衡 

    
 

  论文PDF：   
 

  http://nebelwelt.net/files/20ATC.pdf 

