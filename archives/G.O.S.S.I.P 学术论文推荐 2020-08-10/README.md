 上周末我们推荐了一篇关于client-side钓鱼攻击检测的论文，今天我们推荐的仍然是一篇关于client-side安全研究的论文，来自ICSE 2020会议：   
 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXy1t6qHcV86H0TXnzVsXO6JXTJ5SXswiaEvoyUicGDYUj3mrJ9BFu7keg/640?wx_fmt=png) 

    
 论文作者关注了当今商业应用场景越发复杂的情况下，尽管大家都知道client-side code是可被篡改的，但是仍然会有开发者把关键的、不该放在客户端的逻辑错误地部署在可被用户攻击的位置。作者于是就研发了一套动态监测这种客户端存在关键逻辑可被篡改的情况，可以非常轻量级地检测出这类漏洞。作者对200个流行的网站进行了检查，发现其中23个网站（包括 我们不可访问的 纽约时报、Youtube等）中存在27个漏洞（bypass paywalls, disable adblocker   
 detection, earn reward points illicitly等等）。下图很清晰地展示了这类漏洞 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXOP5nibGocoF0XTSyJAtuPkIjwYP8lXwDoDx8aHHDg4VibWdF5yUVOdEg/640?wx_fmt=png) 

    
 

  作者设计的检测流程，核心在于监控DOM mutation events以及其call stacks，然后对其进行评分（ranking标准见下表1），找到那些潜在的篡改对象。在找到潜在的篡改对象后，通过动态测试尝试对其进行攻击。 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXlVsywYoyHiaWK6tmXqApBe1sywkLbczS2SfleWBEqPu6OTfeCZEuvrA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXgWjGGD0Ws2DYiaQcAapIx3nFFpnTe3ViaxfMF0PjaWXWfhLKYMWLUniaA/640?wx_fmt=png) 

    
 

  接下来是实验结果 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXVqxsvQhobibUHUicxAt4fOC9gWtmFuSdowjUzMKWpCB8d1Ew1G1zJJzA/640?wx_fmt=png) 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXtIo3c79bH92ibKl6c6zJ4xIM9an5UiaqZSzqjD1PvicpveicFIy6riat3nA/640?wx_fmt=png) 

    
 

  发现的一些具体例子： 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXjFaCgzhkibDFiaiaFXrUiazWzHD3lycyKAzL19AWjFW2iaRO8eRbq39Z1uA/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6odibtjDnzmnj7wplOCAEdHHNXWw9t8AbupO2CH10lKVFOIxBgTHLhrseDyicOfNox7RA7icOncNKRe11w/640?wx_fmt=png) 

    
 

  论文PDF： 

  http://hogunpark.com/papers/ICSE2020-Kim-BusinessTampering.pdf 

    
 

