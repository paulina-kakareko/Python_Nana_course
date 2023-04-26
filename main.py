from helper import validate_and_execute
import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the APP")

number_of_days = ""
while number_of_days != "exit":
    number_of_days = input("Enter number of days and conversion unit: ")
    days_and_unit = number_of_days.split(":")
    number_and_days_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(number_and_days_dictionary)







