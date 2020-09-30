# used in troubleshotting
# rotating files

import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
handler = TimedRotatingFileHandler('timed_test.log',when='s',interval=5, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info('hello world')
    time.sleep(1)

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s- %(message)s',datefmt='%m/%d/%y %h:%m:%s')


logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.critical('critical message')
logger.warning('warning message')

logger =logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# formatter
formatter= logging.Formatter('%(name)s - %(levelname)s - %(message)s ')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter) 

# handler
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('warning message')
logger.error('error message')

