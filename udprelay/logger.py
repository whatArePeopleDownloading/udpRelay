import coloredlogs, logging

def getLogger(name = __name__):
    logger = logging.getLogger(name)
    coloredlogs.install(level='DEBUG', logger=logger)
    return logger

if __name__ == '__main__':
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
