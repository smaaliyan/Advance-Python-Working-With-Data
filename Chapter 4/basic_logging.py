import logging

logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

logging.debug("This is a Debug level massage")
logging.info("This is a Info level massage")
logging.warning("This is a warning level massage")
logging.error("This is a error level massage")
logging.critical("This is a critical level massage")

string = "Aaliyan"
integer = 22
logging.info(f"My name is {string} and I am {integer} years old")