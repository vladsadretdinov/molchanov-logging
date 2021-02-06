import logging

logging.basicConfig()
# logger = logging.getLogger()
# print(logger)

app_logger = logging.getLogger('app_logger')

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)
print(app_logger)
# print(app_logger.parent)
# root.app_logger
print(app_logger.handlers)

formatter = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(formatter)

utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')
# utils_logger.propagate = False # propagation
print(utils_logger)
# print(utils_logger.parent)
# root.app_logger.utils_logger
print(utils_logger.handlers)

print()
print('root handlers', app_logger.parent.handlers)
print()


def main():
    utils_logger.debug('Hello worlds')


if __name__ == "__main__":
    main()
