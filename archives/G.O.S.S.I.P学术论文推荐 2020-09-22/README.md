 今天给大家推荐的论文是来自EuroS&P 2020的针对代码重用攻击的防御研究的论文。 

  ![]() 

  目前针对代码重用攻击的防御措施除了ASLR和CFI外，比较流行的方式是移除代码里的不必要代码，既能可以重用的代码还能简化CFI。目前常用的库定制 (Library customization)方法就是移除程序加载的库中没用到的函数，但无法移除例如内存分配、进程管理、文件系统操作等关键操作函数，但根据程序实际需要来限制一些关键API函数的接口的API特化 (API specialization)方法分析存在困难，静态分析函数参数较为复杂且一些参数是运行时确定的。 

  本文作者的目标就是将API特化中对关键系统函数参数的的限制范围扩大。其基本假设是应用程序用到的系统调用和应用程序代码实际用到的系统调用的语义是不同的。在威胁模型中，假设攻击者可以劫持控制流，并且能进行ROP攻击（不考虑Data-only attack）affire的保护依赖于已有的Software debloating技术，例如Library debloating，因此假设Library debloating已经部署。假设CFI已经部署，这样攻击者不能直接跳过check；假设API checkpointing这样的技术已经部署。 

  函数特化这个环节的目标是创建多个API函数的特化版本，这些特化的函数只能在特定的地方调用。CFI限制了函数只能在合法的Call site调用。Saffire基于CFI，进一步限制了函数在不同上下文下被调用时的参数值。SAffire的方法框架如图1所示： 

  ![]() 

  总共三类已知的参数类型：1) 硬编码参数，例如flags、buffer size等；2) Value sets，不同的控制流会设置不同的参数，这些数据中有可以被静态确定的；3) Value ranges，一些特殊的上下文，例如循环里，参数值可以表示为Range。静态分析中，利用IR的控制流信息来回溯函数的调用者，分析在回溯到main或者找到了静态值结束。 尽管很多参数可以静态决定，但是作者通过实验发现有近一半的参数只能在运行时确定。 对于这些值，作者将其哈希后存在Shadow memory里。 

  ![]() 

  Saffire的实现是作为LLVM8的Transformation pass形式，在64位Ubuntu19.04上进行测试。Saffire的输入是合并后的bitcode。Saffire对目标API进行保护，通过后向数据流分析实现。作者用17个真实世界的ROP以及3个完整函数重用的利用进行了评估，Saffire可以成功防御这些攻击，并且引入的开销可以忽略不计。 

  ![]() ![]() 

  原文链接：https://www3.cs.stonybrook.edu/~mikepo/papers/saffire.eurosp20.pdf 

    
 

