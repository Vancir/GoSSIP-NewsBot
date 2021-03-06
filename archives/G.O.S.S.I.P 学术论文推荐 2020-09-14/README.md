 我们知道在HTTPS应用的过程中，Let's Encrypt免费证书大大推进了HTTPS的普及，今天我们给大家介绍一篇NDSS 2020上的论文，介绍了一套证书撤销机制Let's Revoke， ** 我们会在9月15日中午12点（北京时间）直播本论文的讨论会，欢迎大家收听，腾讯会议的会议 ID：180 866 275 ** ， ** 入会链接 https://meeting.tencent.com/s/wn4PxLyJxJSV ** ： 

  ![]() 

    
 

  **   
 ** 

  在本论文中，作者设计了Let’s Revoke证书撤销机制，并对该机制进行了全面的评估。 结果表明，该机制与其他机制相比需要更少的存储和网络带宽。 

  

   LET’S REVOKE SYSTEM DESIGN
---------------------------

 ###  Design Description

 ####  数据结构：

  *   Revocation IDs   
 用来标识一张证书的撤销情况。举例， Let’s Encrypt : March 1, 2018 : 24561   
 包含了三个部分，前两个部分是颁发的CA和过期的日期，第三部分是过期编号。撤销编号由CA指定。 

 
 *   Certificate Revocation Vectors（ ** CRV ** ）:   
 Let’s Revoke维护了一个CRV的数据库。CRV使用一个比特位来标识证书的状态。 

 
   CA的操作 & 客户端的操作   
 

  *   ADD 方法 CA生成撤销的列表，客户端使用ADD方法添加到本地 

 
 *   OR 方法 CA使用OR方法对数据库进行更新 

 
 *   NEW 方法 使用NEW方法进行备份 

 
   要检查证书的吊销状态，客户端首先访问由证书的颁发CA和到期日期指示的正确CRV。然后，客户端通过验证索引RN上的位来确定证书的吊销状态。 

  下图 所 示 的是一个例子：   
 ![]() 

 ### 

  对于证书的更新，Let 's Revoke支持三种用于更新的方法，并且一般选择最小化带宽成本的方法。如果撤销的总数小于0.1%，就使用ADD方法，如果超过了一般，就会使用NEW方法，对于其他的情况使用OR方法。该方法节省了更新证书时所需的网络带宽。 

  ![]() 

  作者还探讨了多个CA设置CRV之间的影响，结果表明，他们之间不会产生影响CA。 ![]() 

 ### 

    
 

  COMPARING REVOCATION STRATEGIES
--------------------------------

 ### 

  作者的评估标准主要是设备存储和网络。结果如表二所示。 虽然前三种方法所需要的存储空间较小，但是不能覆盖所有的撤销情况。 

  ![]() 

  图3总结了所有撤销百分比的存储需求，而图4显示了在日常使用中可能发现的撤销百分比较低时的比较。 

  ![]() 

 ### 

  VIABILITY SIMULATIONS
----------------------

  为了进一步验证CRV的性能，作者进行了吊销模拟，以表明CRV可以用于日常证书撤销检查，并可以扩展用于大规模撤销事件和数量更大的证书空间。 

  作者使用Censys.io收集了截至2018年3月21日的全球证书空间的相关吊销数据。作者首先删除了重复的，过期的，私有的，无效的证书来过滤此数据集，保留了8410万个证书。其次，作者将具有CRL节点的证书与仅具有OCSP节点的证书分开。作者确定了475个没有任何撤销终结点的不可撤销证书，并将它们也从数据集中删除。最后，作者扫描了其余证书以确定它们的撤销状态。   
 

    
 

  ![]() 

  作者考察了以下几个方面： 

  *   当前撤销的空间 经过压缩和优化以后，大小为5MB，且每次更新只需要25KB。 

 
 *   大规模撤销的情况 作者模拟了heartbleed事件而导致大规模证书撤销的情况，并发现存储需求增加到10.8MB，带宽为每天150KB。 

 
 *   日益增长的撤销空间 Let’s Revoke能够随着不断增长的证书空间优雅地伸缩。 

 
   ![]() 

  SECURITY ANALYSIS
------------------

  作者进行了安全性分析。作者假设了一个威胁模型，活跃的网络攻击者可以在其中创建，修改和阻止消息。攻击者有两个目标：(1)强制客户接受已撤销的证书;(2)强制客户认为有效的证书已被撤销。 

  *   Accept a Revoked Certificate 攻击者可以通过阻止客户端更新CRV并得知证书已被吊销，来迫使客户端接受吊销的证书。攻击者实现攻击有两种方法：首先可以通过修改CRV来隐藏历史撤销信息，但是在Let’s Revoke机制下，客户端通过在每次更新时比较CRV来保证保留了先前的撤销；其次是阻止CA的流量，但是由于Let’s Revoke是基于推送机制的，一旦CA不能及时更新，便可被发现。 

 
 *   Revoke a Valid Certificate 攻击者还可以强迫客户相信有效证书已被撤销。攻击者实现攻击有两种方法：首先是获得证书的所有权，在这种情况下攻击者需要知道证书的私钥；其次是修改CRV，但是如前面所述，这种情况无法实现。 

 
     
 

  论文PDF：   
 

  https://www.ndss-symposium.org/wp-content/uploads/2020/02/24084.pdf 

