
from config import config as conf, setting
from config import ReqType
from log import ACOLogger


def log():
    log = ACOLogger()

    # Stream.Info
    # File.Debug
    log.setLogger("appuser")
    log.logger.debug("debug-appuser")
    log.logger.info("info-appuser")
    log.logger.warn("warn-appuser")
    log.logger.error("error-appuser")
    log.logger.critical("critical-appuser")

    # Stream.Info
    log.setLogger()
    log.logger.debug("debug")
    log.logger.info("info")
    log.logger.warn("warn")
    log.logger.error("error")
    log.logger.critical("critical")


def config():

    print(conf)
    print(conf.type is ReqType.MONITOR)
