import logging
 


def get_batch_logger(logdir, project_name, loglevel, backupcount,
                     name=__name__):
    """
    Get rotating file logger for storing logs of mirroring of given project.
    :param logdir: log directory
    :param project_name: name of the project
    :param loglevel: logging level
    :param backupcount count of log files to keep around
    :param name name of the logger
    :return logger
    """

    logger = logging.getLogger(name)

    logfile = os.path.join(logdir, project_name + ".log")

    handler = RotatingFileHandler(logfile, maxBytes=0, mode='a',
                                  backupCount=backupcount)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s: "
                                  "%(message)s", '%m/%d/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    handler.doRollover()

    logger.setLevel(loglevel)
    logger.propagate = False
    logger.handlers = []
    logger.addHandler(handler)

    return logger

get_batch_logger()