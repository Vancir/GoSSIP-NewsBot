 我们之前推荐过一篇ISSTA 2020会议上关于ARM反汇编工具的比较的研究论文（G.O.S.S.I.P 学术论文推荐 2020-06-22），今天我们继续回到ISSTA 2020，看看另一篇反编译器比较的研究论文： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQ2Rwcg8RF5orTBpOCYhP9GFGwjibqwsHmV24VAXVibXw7GYqwaCGCXf8w/640?wx_fmt=png) 

    
 

    
 

  反编译器是安全分析人员的心头最爱，离开了反编译器，可能很多逆向工程师都会吃不香睡不好，那么反编译器哪家强？作者研究了IDA-Pro （Hex-rays），JEB3，RetDec以及Radare2/Ghidra，从多方面比较了这四个反编译器的特点 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQBk3MO2LDnicvCa6fxmGDPvppEqXteyBCibn5Bd5vMGOMxyR5bwDpXq8Q/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQzEuOMM08XYWAszjg4AT3mNEkWWUomeWyWXY60XicK8QibDaRIooEQmkQ/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQdEpuzJEaBjewwc49lRoQFHDS7cOnJVETavibtK6mNsdDK8lewuJyk0A/640?wx_fmt=png) 

  作者借用了已有的用于测试编译器的技术Equivalence Modulo Inputs (EMI) Testing来评估反编译能力，然后用Csmith工具生成了1000个程序来测试4家反编译器 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQic4FicK4D4XHZISuAgvic0IgibTvAoxRuzjFF7udSTbxVY3I8ARNLibCojg/640?wx_fmt=png) 

  结果表明，虽然各家反编译器都有很多毛病，但是作者认为JEB3是表现最好的   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQe9TDVTMHGyOZVOHx5vDtywI4NSIu2BuYYhALg3CpyygwvrpUT4ZRRA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibPUkPILR9DOEEFH4UhWucQXDhYw0wkeu1b9ubniaMV2Ypy2Hl3nVOMzyLthueLiad6WbSZNjBdm1yw/640?wx_fmt=png) 

    
 

  引用G.O.S.S.I.P 学术论文推荐 2020-06-22的话：尽管各种工具在面对纷繁芜杂的二进制代码的时候表现不一，各有千秋，但是我想说的是，如果有钱，请给我一套JEB3授权吧！ 

    
 

  论文PDF： 

  https://dl.acm.org/doi/abs/10.1145/3395363.3397370 

