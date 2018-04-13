from enum import Enum
import logging
import logging.config

# 请求类型


class ReqType(Enum):
    LIST = 1
    MONITOR = 2
    TEST_CONFIG = 3
    TEST_LOG = 4


# 请求参数配置
class Config:

    def __init__(self, logPath="../log/office-auto-close.log", type=ReqType.MONITOR, duration=180, logList=False):

        self.logPath = logPath
        self.type = type
        self.duration = duration
        self.logList = logList

    def __str__(self):
        return "{{\"logPath\": {},\"type\": {},\"duration\": {},\"logList\": {}}}".format(self.logPath, self.type, self.duration, self.logList)


# 服务配置
class Setting:
    def __init__(self):
        # 监听类型
        self.classes = {
            "bosa_sdm_msword": [],
            "#32770": [],
            "NetUIHWND": [],
            "NUIDialog": ["NetUIHWND", "NetUICtrlNotifySink", "RICHEDIT60W"],
            "bosa_sdm_XL9": [],
        }
        # 对应异常类型
        self.types = ["DOC.密码|文件损坏", "文件损坏|保存失败|打印机不可用",
                      "未注册", "PPT.密码", "DOC.密码|选择打印机"]
        # 兼容类型的窗口标题
        self.titles = ["Microsoft Word", "Microsoft Excel",
                       "Microsoft PowerPoint", "密码", "打印机设置"]
        # 日志配置
        self.logConfig = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s %(levelname)10s %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': logging.INFO,
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
                'stdFile': {
                    'level': logging.DEBUG,
                    'formatter': 'standard',
                    'class': 'logging.FileHandler',
                    'filename': '../log/office-auto-close.log'
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': logging.INFO,
                    'propagate': False
                },
                'appuser': {
                    'handlers': ['stdFile'],
                    'level': logging.DEBUG,
                    'propagate': True
                },
            }
        }


# 全局参数
config = Config()
setting = Setting()
