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
            'formatter': 'standart_format'
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

    # 'filters': {},
    # 'root': {},  # '': {}
    # 'incremental': True
}
