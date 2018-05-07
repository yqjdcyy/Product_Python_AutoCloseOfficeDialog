import getopt
import sys
import test

from config import config as conf
from config import ReqType
import windows


def main():

    # opts
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hlt:d:p:",
            ["help", "logList", "type=", "duration=", "logPath="])
    except getopt.GetoptError as err:
        print(str(err))
        help()
        sys.exit(2)

    # analyze
    for key, val in opts:
        if key in ('-h', "--help"):
            help()
            sys.exit()
        elif key in ('-l', "--logList"):
            conf.logList = True
        elif key in ('-t', "--type"):
            conf.type = ReqType(int(val))
        elif key in ('-d', "--duration"):
            conf.duration = val
        elif key in ('-p', "--logPath"):
            conf.logPath = val
        elif key in ('-c', "--configPath"):
            conf.configPath = val
        else:
            help()

    # switch
    if conf.type is ReqType.LIST:
        windows.lst()
    elif conf.type is ReqType.MONITOR:
        windows.handle()
    elif conf.type is ReqType.TEST_CONFIG:
        test.config()
    elif conf.type is ReqType.TEST_LOG:
        test.log()

# 请求参数


def help():
    print(
        "monitor.exe\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}".format(
            "-h|--help\t帮助文档",
            "-l|--logList\t是否打印当前窗口列表",
            "-t|--type\t请求服务类型\n\t\t1:\t当前窗口列表\n\t\t2:\t启用监控\n\t\t3:\t测试参数化运行状态\n\t\t4:\t测试日志打印",
            "-d|--duration\t运行休眠时长",
            "-p|--logPath\t日志输出文件的绝对路径"))


if __name__ == "__main__":
    main()
