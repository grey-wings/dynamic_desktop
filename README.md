# dynamic_desktop  
code文件夹是试验版（仅备份），version0.1是正式（但是没测试过，所以0开头）版。  
[原理和部分实现参考链接](https://blog.csdn.net/hhladminhhl/article/details/119902562?spm=1001.2014.3001.5506)  

能够实现用MP4格式文件作动态壁纸，原理是在图标一下桌面以上创建一个窗口用于播放视频。  
可能存在一些bug（没测出来），暂时没有更新计划。  
主要是写着玩  

[窗口句柄的获取参考教程](https://blog.csdn.net/freeking101/article/details/88249944)   
[pyinstaller文档](https://pyinstaller.org/en/stable/usage.html)  

生成exe文件所用命令：  
```
pyinstaller -i ../../favicon.ico -D --noconsole --distpath ./release/ddplay/ddplay.dist --workpath ./release/ddplay/ddplay.build --specpath ./release/ddplay  ddplay.py
``` 
```
pyinstaller -i ../../favicon.ico -D --noconsole --distpath ./release/DdMainUI/DdMainUI.dist --workpath ./release/DdMainUI/DdMainUI.build --specpath ./release/DdMainUI DdMainUI.py
```  
执行目录为version0.1  
