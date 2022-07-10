# dynamic_desktop  
code文件夹是试验版（仅备份），version0.1初版，version1.0是正式版，很长一段时间内不会再更新。    
[原理和部分实现参考链接](https://blog.csdn.net/hhladminhhl/article/details/119902562?spm=1001.2014.3001.5506)  

能够实现用MP4格式文件作动态壁纸，原理是在图标一下桌面以上创建一个窗口用于播放视频。  
可能存在一些bug（没测出来），暂时没有更新计划。  
主要是写着玩  

[窗口句柄的获取参考教程](https://blog.csdn.net/freeking101/article/details/88249944)   
[pyinstaller文档](https://pyinstaller.org/en/stable/usage.html)  


## 原理  
桌面图标SHELLDLL_DefView本来在Progman窗口下：  
![image](https://user-images.githubusercontent.com/74122331/178148371-fb943122-bce1-44f8-be0c-fb77296e5559.png)  
windows有多个WorkerW窗口。对Progman发送消息0x052C（为什么是这个数字不知道）可以让SHELLDLL_DefView转移到一个workerW下面（这个workerW是新生成的还是本来就有的就不知道了），记这个workerW窗口为h。同时还会生成一个Z序在这个workerW之后的workerW窗口，记为hwnd_WorkW_next。只要找到这个hwnd_WorkW_next，生成一个窗口用于播放视频文件，并将窗口挂在hwnd_WorkW_next的子节点即可。  
