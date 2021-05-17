import os
import errno
import logging
import datetime
import inspect
import functools

from base import tests_base


def automation_logger(logger_):

    def decorator(func):

        @functools.wraps(func)
        def log_wrapper(*args, **kwargs):
            cls_ = _get_class_that_defined_method(func)
            try:
                cls_name = cls_.__name__
            except AttributeError:
                cls_name = ''
            try:
                f_name = func.__name__
            except AttributeError:
                f_name = ''
            try:
                logger_.info(" {0} --> {1}".format(cls_name, f_name))
                return func(*args, **kwargs)
            except Exception as e:
                err = f_name + f" The {f_name} throws an exception: {e.__class__.__name__} {e.__cause__}"
                logger_.fatal(err, exc_info=True)
                raise e

        return log_wrapper

    return decorator


def _get_class_that_defined_method(method):
    if inspect.ismethod(method):
        for cls in inspect.getmro(method.__self__.__class__):
            if cls.__dict__.get(method.__name__) is method:
                return cls
        method = method.__func__
    if inspect.isfunction(method):
        cls = getattr(inspect.getmodule(method),
                      method.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        if isinstance(cls, type):
            return cls


def create_logger(name='TEST_GAME', level='DEBUG'):
    log_file = _create_log_file()
    logger_ = logging.getLogger() if name is None else logging.getLogger(name)
    logger_.setLevel(level)
    format_ = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format_)
    log_file = logging.FileHandler(log_file)
    log_file.setFormatter(formatter)
    log_file.setLevel(level)
    logger_.addHandler(log_file)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger_.addHandler(console_handler)
    return logger_


def _create_log_file():
    cur_time_stamp = int(datetime.datetime.today().timestamp())
    filename = str(cur_time_stamp) + "_automation_test.log"
    path = tests_base + "/repository/logs/"
    message = " --- AUTOMATION LOG STARTED: "
    cur_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not os.access(path, os.F_OK) or not os.path.isdir(path) or not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(path)
            with open(path + filename, "w+") as f:
                f.write(message + cur_date)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(path + filename, "a") as f:
        f.write(cur_date + message + "\n")
    return path + filename


logger = create_logger()
