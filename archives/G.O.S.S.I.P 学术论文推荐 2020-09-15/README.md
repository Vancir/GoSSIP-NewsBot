 今天我们给大家推荐的论文是中科院出品的关于漏洞检测的Usenix Security 2020研究论文 

  ![]() 

    
 

  与单纯的漏洞检测视角不同，这篇论文着眼于漏洞及其补丁，旨在以较高的精度实现对recurringvulnerabilities（重复出现的漏洞）的检测。Recurring vulnerability就是指在不同版本或系统中出现的未被及时修补的漏洞，通常是由于重用的代码库和共享的代码逻辑导致的。 

  

  这类漏洞的检测过程中涉及到三类对象，分别是vulnerable function（V），patched function（P）和target function（T）。目前有两类方法进行检测：clone-based和function matching-based。然而由于V、P之间较高的相似性以及V、T之间较低的相似度，导致这两种方式存在较高的误报和漏报。 

  

  为了提升recurring vulnerability检测的精度，作者将security patch纳入考虑，通过程序切片从vulnerable function及patched function中提取语法和语义级别上的漏洞、补丁签名，然后将与漏洞签名匹配但与补丁签名不匹配的目标函数标记为潜在漏洞。该方法的流程如图2所示，基于该方法，作者实现MVP (Matching Vulnerabilitieswith Patches)工具。 

    
 

  ![]() 

    
 

  作者设计的函数签名获取主要有三个步骤： 

  2.   首先解析代码并生成code property graph【出自S&P’14的Modeling and discovering vulnerabilities with code property graphs】，这种graph集合了抽象语法树（AST）、控制流图（CFG）和程序依赖图（PDG）； 

 
 4.   进行函数的抽象和规范化，即识别出AST中的形式参数、局部变量和字符串，使用PARAM、VARIABLE和STRING替代； 

 
 6.   生成函数签名，这里的函数签名设计中，作者结合了函数的statements及其之间的依赖关系。 

 
     
 

  ![]() 

    
 

  ![]() 

    
 

  对于漏洞与补丁的签名生成，首先需要从commits中找到补丁修改的函数，然后在函数的statement级别进行分析，在PDG上进行后向的程序切片和与slicing criterion类型相关的前向切片，尽可能准确地找到安全补丁及对应的漏洞。最后，依据下面的公式计算漏洞和补丁的签名： 

  ![]() 

  作者在包含25377个安全补丁的十个开源系统对MVP进行了评估，并且与state-of-the-art方法进行了对比，包括clone-based方法（ReDeBug和VUUDY）、function matching-based方法（SourcererCC和CCAligner）、learning-based（VulDeePecker和Devign）以及商用工具（Coverity和Checkmarx）。结果显示，MVP在精度上明显优于clone-based和function matching-based漏洞检测方法，且MVP检测到的一些漏洞无法通过learn-based和商用的两种工具借助通用漏洞检测方法来检测。最后，MVP检测到97个新漏洞，并分配到了23个CVE。 

    
 

  ![]() 

  ![]() 

  ![]() 

  ![]() 

    
 

  ![]() 

    
 

  论文PDF： 

  https://www.usenix.org/system/files/sec20-xiao.pdf 

