import logging.config

settings = __import__('04-settings')
logging.config.dictConfig(settings.logger_config)

app_logger = logging.getLogger('app_logger')

words = ['new house', 'apple', 'ice cream', 3]


def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            app_logger.exception(f'Exception here, item={item}')
            pass


if __name__ == "__main__":
    main()
