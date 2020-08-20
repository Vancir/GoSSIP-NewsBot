 一年又一年！我们的论文推荐从情人节开始，已经积累了许多人森经验和姿势水平，今天我们选择一篇来自香港的研究论文 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JpficuzjxywcQZnjsTmTJkeRPCyibLjuqqCicz4Xur6qicTH153YgxOichcg/640?wx_fmt=png) 

    
 

  本文讨论了Android系统上一类特殊的link——app link的安全问题。先说说背景知识，在讨论app link之前，Android系统上已经存在deep link (e.g., yelp:///career/home) 这种特殊的link，Android系统允许deep link将控制流从一个网页导向一个手机上的app，实现便捷的导向机制。与deep link不同的是，app link必须类似http(s)://...这样的格式，并且系统强制了针对app link的相关verification。简单地说，app link就是让用户在安装了对应app的情况下就直接访问app内容，否则就访问web内容的一种机制（https://developer.android.com/training/app-links） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JB8b02Fb0QXxBN0FF4ztfHoeVMhUUriapibOmUqvuyaLB9nAMnWFP3K7A/640?wx_fmt=png) 

    
 

  作者进一步研究发现，随着新版本的Android系统上instant app（https://developer.android.com/topic/google-play-instant，可翻译为“快应用”？即无需安装就可使用的轻便app，MIUI目前也有类似的实现）的兴起，app link这个机制变得危险起来，由于instant app的存在，针对app link的verification可以很容易就被绕过 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JJsmyKIiaQ8tYKicsIjFKXqy0uIIYJicuwrWH1CDzKycicUudEDicE84icgdg/640?wx_fmt=png) 

    
 

  作者研发了一个名为 ** MIAFinder ** 的工具，对40万个Android app进行了检查，发现其中30%的app都可能受到和app link相关的三类攻击：link hijacking   
 with smart text selection (STS), link hijacking without STS, instant app hijacking的影响 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JuErOWUyMu9ntPibNFREAwKTd1lt86NpzVAFGJIYvibxfWoGxmwDPxgyw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6J9ibDtqx13KicesZ4VgiaPib7oe0g0Opjj8BGLzhoC3wicL3oJJicNzRbk8YQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JOLCDIZwD7tAawQFDorWQG50T45vwheGyK9SUOzqhldzkvkP5XpPh2A/640?wx_fmt=png) 

    
 

    
 

  MIAFinder用静态分析来检查三类攻击 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JAsCOUmUSRhszoxbafX5u2YIAsvLicSR4ITFnaI3MaLeg3Zgibs0L0Lzg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JuC0qDFQo2JoKCYtXRVKYx5iczsgTNV6eD2pQRGVtH6IFz3l6T4eyR3A/640?wx_fmt=png) 

    
 

  研究结论总结：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JePic6KplbvkLh4LFJ9CXdSiaBQzicBPKfYTR3yTsrjPmgdTf0e0H08Vyg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6Jvk7Ucib8goSiaQBQoJJPeMzAsKj3PP0oWjoRCiaCTKwDMdyibsxErOUl6w/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6Jds4GjM4yLNw5SnibP32ly86ZqCDziaS7LWnLviab7WToUmUSdiaodVSpIA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odiczGEgDycYBduoH3zZ59L6JRPHRbEEibClcL3ru5T9F4u0EubbIFOPoLQSLcEAYjY1edjWmrHsfdow/640?wx_fmt=png) 

    
 

  论文PDF： 

  https://www.chrisyttang.org/research/publication/paper/fse-20.pdf 

    
 

  MIAFinder开源： 

  https://sites.google.   
 com/view/instant-app-attacks 

