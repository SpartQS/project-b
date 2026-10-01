import logging


def get_logger(name="project-b"):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)