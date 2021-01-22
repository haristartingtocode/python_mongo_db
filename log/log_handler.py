""" Generic class for handling logs messages """

# Standard modules.
import logging
import os


def _create_logging_directory(path):
    """ Create logging directory if it doesn't exist.

    :param path: The absolute path of the directory.
    :return:     None
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    except OSError:
        pass


class LogHandler:
    def __init__(self, path: str = __name__, file_name: str = 'bootstrap'):
        _create_logging_directory(path=path)
        full_path = '{}{}.log'.format(path,file_name)

        # Create filehandler.
        self._file_handler = logging.FileHandler(full_path)
        self._level = logging.DEBUG
        self._file_handler.setLevel(self._level)

        logging.root.setLevel(self._level)

        # Create log formatter.
        self._format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-08s - %(message)s')
        self._file_handler.setFormatter(self._format)

        # Set logger paramaters.
        self._logger = logging.getLogger(file_name)
        self._logger.addHandler(self._file_handler)

    def info(self, msg):
        self._logger.info(msg=msg)

    def warning(self, msg):
        self._logger.warning(msg=msg)

    def error(self, msg):
        self._logger.error(msg=msg)

    def exception(self, msg):
        self._logger.exception(msg=msg)

    def debug(self, msg):
        self._logger.debug(msg=msg)

    def critical(self, msg):
        self._logger.critical(msg=msg)
