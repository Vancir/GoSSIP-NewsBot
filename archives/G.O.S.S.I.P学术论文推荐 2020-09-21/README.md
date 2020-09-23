 上周9月17日我们推荐的论文MemLock是针对内存消耗漏洞的fuzzer，今天我们推荐的这篇来自RAID 2020的论文则是针对内存破坏漏洞中的UAF类型漏洞。 

  ![]() 

  Use-After-Free (UAF)漏洞是由于内存释放后对应的指针没有被清除，导致其成为一个悬空指针（dangling point），有可能被攻击者利用。具体来说，一个UAF漏洞表现为对于同一个内存对象的分配（alloc）、释放和使用（通常是dereference），例如list-1的例子。 

    
 

  ![]() 

  目前的fuzzer在针对UAF的检测上仍然存在困难：由于UAF本身的复杂性，其alloc、free、use需要对同一内存对象的有序访问，coverage-based对于fuzzer的指导就不再奏效，Directed fuzzer缺乏对次序的考虑也无法取代好的效果；而且UAF未必会产生crash，这使得很多fuzzer难以发现。于是作者就研究了Binary-level Directed Fuzzing的技术UAFUZZ，其大体结构如图2所示。 ![]() 

  ![]() 

  在插桩阶段，UAFUZZ作为directed fuzzer，在VALGRIND生成的bug trace上做了扁平化作为target，从而适配轻量级的插桩及fuzzing，如图1到图5的转化。 

  ![]() 

  ![]() 

  在fuzzing过程中，作者设计了三种metric： 

  2.   Target Similarity Metrics，用于衡量种子的执行路径和目标UAF的bug trace之间的相似性，分为图4中的四种粒度，并组合成P-3TP-B metric。 

 
 4.   UAF-based Distance Metric：与传统的距离计算方式不同，UAFUZZ除了考虑常规的call graph中的调用关系，还考虑了调用次序（降低这些alloc、free、use之间的edge权重），如图5所示，降低了红色edge的权重。 

  ![]() 

 
 6.   Cut-edge Coverage Metric：对于coverage来说，通常会在基本块层面进行计算，但是这样开销过大，而仅从函数层面又精度过低。于是UAFUZZ中和这两种方式，仅计算关键决策节点（也就是条件跳转）的edge层面覆盖率，具体如算法3、4所述。 

  ![]() 

 
   于UAF错误缺乏明显现象，因此必须将directed fuzzer生成的所有种子预先发送到bug分类程序（如VALGRIND），以确认它们是否是bug触发输入，但大量的种子会产生大量开销。UAFUZZ利用target Similarity来预先选出可能触发bug的种子，仅对这些种子进行bug分类，大量减小了时间开销。最后，UAFUZZ的实现如图6所示。 

  ![]() 

  文章针对bug reproduction，对比一些state-of-the-art的directed fuzzer，展开了评估，在故障检测率、暴露时间、错误分类方面，UAFUZZ都有显著的优势。而且UAFUZZ在补丁测试方面，在Perl、GPAC和GNU中发现了30个新的bug（其中7个CVE）。最后作者也开源了一个专门针对UAF的fuzzing的大型benchmark：https://github.com/strongcourage/uafbench 

    
 

  ![]() 

    
 

  ![]() 

  ![]() 

  原文链接：https://arxiv.org/pdf/2002.10751.pdf 

    
 

