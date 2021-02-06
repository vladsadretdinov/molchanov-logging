import logging


class NewFuncFilter(logging.Filter):
    def filter(self, record):
        # print(dir(record))
        print(record.oleg_name)
        return record.funcName == 'new_func'


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
            'filters': [
                'new_filter'
            ]
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': [
                'console_handler'
            ],
            # 'propagate': False
        }
    },

    'filters': {
        'new_filter': {
            '()': NewFuncFilter  # filters.py > import filters > filters.NewFuncFilter
        }
    },
    # 'root': {},  # '': {}
    # 'incremental': True
}
