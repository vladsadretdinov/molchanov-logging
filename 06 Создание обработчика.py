import logging.config

settings = __import__('06-settings')
logging.config.dictConfig(settings.logger_config)

app_logger = logging.getLogger('app_logger')


def new_func():
    name = 'oleg'
    app_logger.debug('Enter in to the new_func()', extra={'oleg_name': name})


def main():
    app_logger.debug('Enter in to the main()')


if __name__ == "__main__":
    new_func()
    main()
