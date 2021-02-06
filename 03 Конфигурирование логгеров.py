import logging.config

settings = __import__('03-settings')
logging.config.dictConfig(settings.logger_config)

app_logger = logging.getLogger('app_logger')


# app_logger = logging.getLogger('app_logger')
# app_logger.setLevel('DEBUG')

# console_handler = logging.StreamHandler()
# app_logger.addHandler(console_handler)

# # standart_format = logging.Formatter(
# #     fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
# # )
# standart_format = logging.Formatter(
#     fmt='{asctime} - {levelname} - {name} - {message}',
#     style='{'
# )
# console_handler.setFormatter(standart_format)

# file_handler = logging.FileHandler(
#     '03-debug.log',
#     mode='a'  # append - default
# )
# app_logger.addHandler(file_handler)
# file_handler.setFormatter(standart_format)


def main():
    app_logger.debug('Enter in to the main()')


if __name__ == "__main__":
    main()
