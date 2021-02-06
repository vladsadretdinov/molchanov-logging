import logging


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as file:
            file.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,  # отключает все логгеры кроме корневого

    'formatters': {
        'standart_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standart_format',
        },
        'file': {
            '()': MegaHandler,
            'level': 'DEBUG',
            'filename': '06-debug.log',
            'formatter': 'standart_format',
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': [
                'console_handler',
                'file'
            ],
            # 'propagate': False
        }
    },

    # 'filters': {},
    # 'root': {},  # '': {}
    # 'incremental': True
}
