 7月份的尾巴是狮子座，进入到8月之前，我们的论文推荐给大家带来一篇SoK论文   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcCzcxumVDAiabLm88mVe9Fgw7XeGicc0b7A9wjRpYAqaLID7yQLQiarN6w/640?wx_fmt=png) 

  作者研究了最近几年发布的多款二进制代码分析工具：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc8b8yj3ia8BfW2dlibIJb5kfTLPpErP6U3wS57YRzwSjIn5iarFkMxdtYw/640?wx_fmt=png) 

    
 

  具体关注三个问题：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcjBiacvt2rpx7snEN8dlauO6Z2M2GHqCRulNfGfJ4sAemclN2GUsGb6Q/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcITUEXe5olSR5AGd2NtiaMEuKfQw9HZfs0qEwibYHJ69Xp0d0pM7JV6kQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcHEB7BHEp3MRzQVrTqUMYunfPqAMV150V17ZKBLiavY7KnpSGRvapoEA/640?wx_fmt=png) 

    
 

  为了详细评估这些分析工具，作者用了大量的现实二进制代码来进行测试： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc7UfW8RrBPkA6nAmRJflpw5ib3ep6Gh8cW7BIlGnLdwfR7PHQXImZACA/640?wx_fmt=png) 

    
 

  测试的结果和2016年Usniex Security上发表的著名的论文An in-depth 

  analysis of disassembly on full-scale x86/x64 binaries类似，作者认为汇编工具应该简单粗暴（linear disassembly），效果反而好于复杂分析（recursive disassembly） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcSKS3H6d7f9ONKRlMpPHtTrgRGibdmtick6J8yKPdvianvya8sTgB5sALg/640?wx_fmt=png) 

    
 

  接下来是一些误报和漏报的分析：   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc321Eic0E6hVAJK58V6uYl64picxeRnZicGuKlicMkFcckMgLkEUYmicSwKQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc66XFBuVqCXo3meEJc2LIgwaq7fgrCUYoILptMOjIq8iahfX52uc2CRg/640?wx_fmt=png) 

  作者发现在符号化分析中，开源工具的效果比商业工具要更好，但是也部分考虑到有些开源工具（如McSema）是在商业工具（如IDA Pro）的基础上进行的二次分析导致的   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcfI2nIWiatApP2DqOZTO2XL03Mnz0KQgiaiaeic9kgZwT2z28KaKLKhbHibQ/640?wx_fmt=png) 

    
 

  对函数的识别是反汇编工具中一项重要的指标，在这项指标上，IDA再次展示了金元对科研的优势： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc06B0CxDwCCf2tLn8kIAxYzJvST3onIhia6P1Q1BdfevsaR1TsictO8CA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcVEqwcmgnibmWgYvpMiaqB8fo3EC1TKhqburAyv5CtEZNRd9YaThLCf3w/640?wx_fmt=png) 

    
 

  针对控制流图CFG的分析：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDciaG1ljlqEPhqnRdfRaO7lh5lT1q27y4HLdEybpOvhh6kT6fITLJqpgg/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDclLQcCJ3rfEBWDhkZLJkY0L5XUkOt5NwhuswIaOpb1fglCtia3NkYOyQ/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDckoISR2cOL2HURfAFOHb5kibbR8KnLublF3cN3pWLJfwMMHx8cQY4Kcw/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDcZQs0XjoYBFric0OREqj3tHjg9N6Uw90n4W8aFJqJxVH0AfX1ZtNup5g/640?wx_fmt=png) 

    
 

  经过一番比较后，作者得出结论   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9hTkrZkwRCfaWkMMj9LpDc2iadeGib2pHyBI5q5pFiaKBiaVHoe9H2Lz9CtGXRWP2Q17mJKibov1oqQLQ/640?wx_fmt=png) 

  而我们的结论更为简单（这也是G.O.S.S.I.P实际上做的） 

  1. 下载编译和使用各类开源工具 

  2. 拿出2万美元，购买IDA Pro、JEB3和Binary Ninja全家桶   
 

    
 

  祝大家逆向愉快！ 

    
 

  论文PDF： 

  https://arxiv.org/ftp/arxiv/papers/2007/2007.14266.pdf 

