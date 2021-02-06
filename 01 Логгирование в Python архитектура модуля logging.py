import logging
import requests

logging.basicConfig(level='DEBUG',
                    # filename='01-mylog.log'
                    )
logger = logging.getLogger()

logging.getLogger('urllib3').setLevel('CRITICAL')

# print(logger)

# print()
# logger.setLevel('DEBUG')  # logger.setLevel(logging.DEBUG)

# print(logger.level)
# print()

# print(logger.handlers)

# for key in logging.Logger.manager.loggerDict:
#     print(key)

# NOTSET - 0
# DEBUG - 10
# INFO - 20
# WARNING - 30 defalut
# ERROR - 40
# CRITICAL - 50


def main(name):
    logger.debug(f'Enter in the main() func: name = {name}')

    r = requests.get('https://www.google.ru')


if __name__ == "__main__":
    main('oleg')
