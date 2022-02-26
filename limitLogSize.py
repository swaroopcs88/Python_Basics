# how to limit log size in python
import logging
import logging.handlers
logging.basicConfig(filename=logfile.log, level="info", format='%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
logging.info("*************************************************")
