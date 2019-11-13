from os import sep as s
from logging import (
    Logger as Log,
    Formatter,
    StreamHandler,
    FileHandler,
    CRITICAL,
    FATAL,
    ERROR,
    WARNING,
    WARN,
    INFO,
    DEBUG,
    NOTSET,
)


class Levels:
    CRITICAL = CRITICAL
    FATAL = FATAL
    ERROR = ERROR
    WARNING = WARNING
    WARN = WARN
    INFO = INFO
    DEBUG = DEBUG
    NOTSET = NOTSET


class Formats:
    default = '%(asctime)s [%(levelname)s] %(message)s'


class Logger(Log):
    def __init__(
        self,
        name=__name__,
        level=Levels.DEBUG,
        format=Formats.default,
        mode='w',
        file=None,
        stream=True,
    ):
        # create logger
        Log.__init__(self, name)
        self.setLevel(level)
        formatter = Formatter(format)

        if stream:
            # create console handler
            handler = StreamHandler()
            # set handler log level
            handler.setLevel(level)
            # set handler formatter
            handler.setFormatter(formatter)
            # add handler to logger
            self.addHandler(handler)

        if file:
            # create log_file handler
            handler = FileHandler(file, mode)
            # set handler log level
            handler.setLevel(level)
            # set handler formatter
            handler.setFormatter(formatter)
            # add handler to logger
            self.addHandler(handler)

    def get_file_paths_from_log(self):
        file_paths = []
        for handler in self.handlers:
            try:
                file_paths.append(handler.baseFilename)
            except:
                pass
        return file_paths

    def get_log_file_directories(self):
        file_paths = self.get_file_paths_from_log()
        log_directory = []
        for file_path in file_paths:
            try:
                log_directory.append(file_path.rsplit(s, 1)[0] + s)
            except:
                pass
        return log_directory
