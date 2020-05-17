# time_analysis
其实大多数人对自己的一天都没有一个清醒的认知，完美的一天是什么样？  ins风的早餐，晨起跑步，日间高效的工作时间，下班后朋友的聚会，上新的电影，面膜与氤氲的泡澡时间，最好要有一杯红酒……  


明白时间管理的意义就是在于深刻的洞察到了这样完美的一天需要远超过72h，或许我能帮助你认识到所谓不差的一天，还行的一周，挺好的一年，以及完美的一生……    文艺的部分过去了，我们开始干货。


林林的完整的时间管理路线包括规划时间（时间日志），记录追踪（toggl），进入到心流模式（Forest），时间记录汇总分析（时间清单+林林的python小程序），这里存放的是林林的python小程序哦~~❤

# time_process_day.py
在mac电脑下打开terminal，在windows电脑下打开anaconda promt，进入到存储python脚本的地方。

执行：

  $ python time_process_day.py -i ./time_list/20200411-林林小公主的时间记录清单.csv -o ./20200411-result/


说明 -i 后面接存放时间清单的全路径，./的意思是当前文件夹下，大家可以用tab键进行补全。

-o 后面为产生的分析结果图片存放的文件夹，大家可以自己设置一下。

运行完了之后大家会在文件夹下发现一个名字为 20200411-result的文件夹里面可以得到对应的3张时间分析图

# time_process_week.py
在mac电脑下打开terminal，在windows电脑下打开anaconda promt，进入到存储python脚本的地方。

执行：
  $ python time_process_week.py -d ./time_list/20200411_week_list/ -o ./20200411_week/

说明 -i 后面接存放时间清单文件夹全路径，./的意思是当前文件夹下，大家可以用tab键进行补全。

-o 后面为产生的分析结果图片存放的文件夹，大家可以自己设置一下。

运行完了之后大家会在文件夹下发现一个名字为 20200411_week的文件夹，文件夹下有4张时间分析的图。

关于更多的时间管理的流程，请参考我的公众号推送：

比心心~~
