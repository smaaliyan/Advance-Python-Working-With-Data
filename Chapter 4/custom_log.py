import logging

extra_data = {'user': 'smaaliyan0@gmail.com'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extra_data)


# set the output file and debug level, and
# use a custom formatting specification
fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(filename="custom_output.log",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)

logging.info("This is an info-level log message", extra=extra_data)
logging.warning("This is a warning-level message", extra=extra_data)
anotherFunction()
