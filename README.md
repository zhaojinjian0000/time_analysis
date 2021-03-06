# 时间分析 for Windows 
- 该项目由LotusWang0723/time_analysis修改得，针对适配windows系统，并可以修改桌面壁纸
- [forked from LotusWang0723/time_analysis](https://github.com/LotusWang0723/time_analysis)
- [理论指导为原作者文章](https://mp.weixin.qq.com/s/p2VuPg5YvHs6-uBKp04rOg)
- 在win10下的桌面截图为(安装便笺后，安装方法和win7安装方法见README最后)
![image](https://github.com/zhaojinjian0000/time_analysis/blob/master/ptrsc.png)


## 功能
- 原始的时间统计功能只保留按天统计
- 新增了更换为桌面壁纸功能
- 适配了windows的编码方式，默认为ansi (mac默认是utf-8)
生成壁纸为
![image](https://github.com/zhaojinjian0000/time_analysis/blob/master/wallpaper_new.png)
## 安装
1. 安装python并添加到路径
2. 下载本项目后打开
3. 双击install.bat，安装python包，（直到无问题，无红字）
4. 双击debug.bat，若无问题则可以正确更换桌面壁纸
5. 在debug.bat运行无误后，双击change_wallpaper.bat即可在后台运行，至此安装完毕

---
## 入门使用指南
###### 如何修改内容
- 如何修改某一天的时间表：修改csvs/20210305-zjj.csv，修改后运行change_wallpaper.bat

---
## 进阶使用指南
###### 如何修改内容
- 如何修改壁纸左下方文字：在wallpaper_text.txt中修改，修改后运行change_wallpaper.bat
- 如何修改壁纸左下方文字大小：右键change_wallpaper.bat编辑，在"set  fontsize=40"一行，修改40为想要的值，修改后运行change_wallpaper.bat（注：修改change_wallpaper.bat内的某个值/文本后，需要数值/文本前后都不能留空格）
- 如何修改壁纸背景：修改wallpaper.png，修改后运行change_wallpaper.bat（图片大小变化后，可能导致左下方文字大小异常，按上述修改）
- 如何修改某一天的时间表：修改csvs/20210305-zjj.csv，修改后运行change_wallpaper.bat
- 如何新增一天的时间表：在csvs文件夹内新建"日期-项目名称.csv"，右键change_wallpaper.bat编辑，在"set  name=20210305-zjj"一行，修改20210305-zjj为想要的"日期-项目名称.csv",修改后运行change_wallpaper.bat（注：修改change_wallpaper.bat内的某个值/文本后，需要数值/文本前后都不能留空格）

###### 如何更简便
- 快捷更换

  右键change_wallpaper.bat，选择“发送到“---”桌面快捷方式”

- 自动更换：[使用windows的任务计划程序](https://blog.csdn.net/weixin_42046939/article/details/103886833)
  开始任务自行设置，可以设置为开机自启/每隔30分钟运行一次
  程序或脚本为change_wallpaper.bat的路径，起始于change_wallpaper.bat所在的文件夹

- 对于win10，可以[参考该文章使用便笺](https://jingyan.baidu.com/article/a378c960510893f329283004.html)

- 对于win7，可以[参考该文章使用便笺](https://jingyan.baidu.com/article/4b07be3c8b4d9848b280f35a.html)