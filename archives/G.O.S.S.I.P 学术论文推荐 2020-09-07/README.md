 我们今天要带大家去读一篇关于RISC-V和硬件安全隔离机制相关的Usenix Security 2020研究论文   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHHk3sib6woKlgyZGCjQ2Cib0Sv372kibPavfuvbp7DA6wVAVSNuYsc9Pdw/640?wx_fmt=png) 

    
 

  近年来许多安全研究工作讨论了如何高效实现进程内隔离（in-process isolation），其中一个必要的因素是借助硬件来实现快速的权限切换，Intel在这方面显然走得比较早，提出了MPK机制等，而新兴的RISC-V处理器在开源的机制下也有利于研究者加入类似的特性，本文就基于RISC-V Ariane CPU开发了一套名为Donky的隔离机制（同时也针对Intel MPK做了模拟实现），其核心是在保证高性能的权限切换的情况下，解决MPK这类机制保护能力不够强（MPK的权限切换是在进程中而非内核态实现的，因而容易遭到攻击）的缺点。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarH3dzCCib0zcu2KmLSsWOtJmCY923Xl6A5x3iaAzQLvofTSWFHNSvdGXfA/640?wx_fmt=png) 

  Donky引入了一个domain monitor来保证domain的切换是安全的，由于这个domain monitor运行在用户态而非内核态，因此保证了开销不会很高。在Donky机制支持的环境下，代码可以使用Donky定义的dcalls来切换domain进行不同权限的操作 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHib7H23f4phbo7rLCo5Zq03YPJyZJ8qQ5LuohJpLUPprKJCIoMwY0GAA/640?wx_fmt=png) 

    
 作者给Donky提供了一组API，方便开发者使用Donky机制的同时保证了安全性 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHA7aGkKFCledIPohcckM2wdXTicosLzkTzxrMVJXulfrYMxibUoGI26og/640?wx_fmt=png) 

    
 

  论文比较了Donky和一些已有的硬件支持的隔离机制 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarH9qdjzw2MWNWY8cM8yykV5Q6KyOOZSUibt2hyhF15SFF8vmAfb6iaxUDw/640?wx_fmt=png) 

    
 

  Donky的性能开销也表现得不错   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHHwicR6ybTEnnf690BywVgDia2stgHhVonS0AKTRsQJnibzhwrNxkBHF2g/640?wx_fmt=png) 

    
 

  作者使用Donky对Javascript引擎、三方库特别是密码库进行了安全防护实验，研究表明Donky的性能开销还是可以接受的   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHeLibGbdOrDIHT7WJR2fBPIUcpPTXTTaKAviaCGIMXibRFppsjYI1Cia1vw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od8PW62VhEmva8LaXsfudiarHqaiaUaIcTZ8JmFUG4ygqEasdt2WvGeLnLTmibpIibLm5hLfB4aZFs5K2w/640?wx_fmt=png) 

    
 

  论文PDF：   
 

  https://www.usenix.org/system/files/sec20\_slides\_schrammel.pdf 

    
 

  论文开源代码： 

  https://github.com/IAIK/Donky 

    
 

