 这几天Usenix Security 2020会议正在线上召开，同期举行的还有附属的一些workshops，其中WOOT这个会议中的论文非常有意思，我们今天给大家介绍的是WOOT 2020中一篇关于TEE安全分析的研究论文   
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qCvr1XFeMl3ch0A50sko6nzFv0rP5IU5pjcgSfX4hibh8DibJlR3Wwic1mg/640?wx_fmt=png) 

  这篇论文关注了华为2015-2018年期间发布的TrustedCore TEE系统的安全问题（华为目前已经迁移至iTrustee TEE系统，并关闭了bootloader解锁，对firmware也进行了加密），值得注意的是， ** 在2015年该TEE系统开始启用以后，G.O.S.S.I.P在2016年针对该系统开展了分析，也发现了相关问题并通报了华为，在今天这篇论文公开之后，我们终于可以聊一下这个话题，并附送一个相关安全问题的彩蛋 ** ** （文末见，目前华为的系统中已经全部修复了相关问题） ** 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qC3LQA8OVdrtj5Sx0X82uPWW03r85HNZRGO3qOzsibDZL1icYt1pljQs0w/640?wx_fmt=png) 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qCZ91pXmt9EtYpyF32RAqwvvyNE7biarXsRtxwNerib2OeRB7bPuOj0LWg/640?wx_fmt=png) 

  TEE的一些基本知识，大家都耳熟能详，但是对华为这款TEE系统的安全分析有几个步骤是比较关键的，我们来介绍一下：   
 

    
 

  首先，当时华为的系统采用了一个比较奇怪的设计，即对TA进行了加密。我们在当时分析的时候就指出，TEE系统其实并不需要对TA进行加密，而只需要进行签名，这是因为TEE系统的镜像可能会被逆向，对TA的加载过程就会暴露，实际上并不能有效对抗攻击分析 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qCQuY5ViaTTseT9mMiacThAicTSegiaqFzPHUABgoXVeBAbKvjPq6Zm05fTA/640?wx_fmt=png) 

  华为TrustedCore的保护策略是用一套白盒AES来保护一堆公私钥，然而由于我们可以得到TrustedCore的firmware，我们很容易就发现了这个AES，尽管我们可以破解这款AES，但是当时我们和本文作者一样，用emulator直接执行了一遍这款白盒AES就可解密了（这也说明了该白盒AES的设计并没有考虑设备绑定） 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qC3ge7QbVftryUXibqLeS0vkWsic106a4uJ7WDvuL4micao4T445oHiac4cA/640?wx_fmt=png) 

  通过提取相关的密钥，我们就可以解密那些被加密的TA，并且进行逆向分析，作者在本文中分析了133款firmware images（2015年7月至2018年四月发布），其中119款均可分析出TA的解密密钥 

    
 

  基于这些攻击，作者发现了TrustedCore系统中的KeyStore TA的安全问题，继而攻破了全磁盘加密 

    
 

  作者还公开了相关研究分析的代码： 

  https://github.com/teesec-research/tckit 

    
 

  论文PDF： 

  https://www.usenix.org/system/files/woot20-paper-busch.pdf 

    
 

  论文、slides和视频： 

  https://www.usenix.org/conference/woot20/presentation/busch 

    
 

  最后是彩蛋部分，介绍当时我们发现的一个有意思的安全问题：下图中加密的TA包含了manifest部分和ELF签名部分，在这个设计中，实际上违反了密码学的一个最佳实践，即“需要对消息整体签名，而不是消息的内容签名”。尽管攻击者并不能伪造一个签名，但是由于TA仅仅是针对ELF加密部分的内容进行了签名，我们可以将manifest部分换成另一个合法的manifest（比如从另一个TA中复制一份过来），这样TA的签名和内容能对应，但是解密密钥就错了！尽管如此，我们当时发现这种TA仍然可以通过TrustedCore系统的检查，并被送入到TEE中执行，结果是什么呢？请大家留言竞猜！ 

    
 

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ugr3WBm6od9azzd030OpwAS4nE2KQ4qCn2W4JLjrMfibfJqBE4MvHgBxgJySAFDic9yn6ZphRVial8RKIYic563Odg/640?wx_fmt=png) 

    
 

