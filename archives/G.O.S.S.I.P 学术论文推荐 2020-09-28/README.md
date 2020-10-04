 本文中，作者对TrustZone-assisted TEE Systems中存在的安全问题进行了研究，整理了目前各种TEE的实现中所存在的Attack Surface，并对出现的漏洞进行了归类、讨论了TrustZone-assisted TEE Systems中的缓解措施。文中对比了Qualcomm, Trustonic, Huawei, Nvidia, and Linaro的TEE实现。 

  ![]() 

  Compromising the TEE kernel：攻击者可以通过两条路线攻陷TEE kernel： 

  - REE App→Android OS→Secure Monitor→TEE Kernel; 

  - REE App→TA→TEE Kernel 

  Compromising the REE kernel: REE App→TA，攻击者在compromised TA中可以map NW物理内存，以修改被Linux kernel分配的内存。 

  ![]() 

  作者研究了数个TEE的实现：Qualcomm, Trustonic, Huawei, Nvidia, and Linaro 

  ![]() 

  ![]() 

  作者总结发现其中三个主要的攻击面： 

  - Architectural （eg. 没有ASLR） 

  - Implementation （e.g. 实现上的漏洞，buffer overflow） 

  - Hardware （e.g. side-channel） 

  ![]() ![]() ![]() ![]() 

  例如Microarchitectural Side-Channels层面有三类问题： 

  2.   Leaking information through caches，在TrustZone-enabled处理器上，cache是被secure world和normal world共享。目前已有成功从cache中恢复128bit AES密钥。   
 

 
 4.   Leaking information through branch predictor，现代处理器中有branch target buffer (BTB)用于分支预测，被SW和NW共享，可以通过Prime+Probe leak敏感信息。已有攻击从Qualcomm上的kerstore恢复出256-bit私钥。 

 
 6.   Leaking information using Rowhammer，Rowhammer是一种利用软件引起硬件错误，从而影响DRAM的技术。允许攻击者控制内存读操作，反转物理内存中的bits。当TEE中的RSA private被分配在secure/no-secure内存边界处时，可以在no-secure边界频繁读，造成在secure引入错误，从而corrupt private keys。 

 
   ![]() ![]()   
 

  原文链接：https://www.cs.purdue.edu/homes/pfonseca/papers/sp2020-tees.pdf 

    
 

