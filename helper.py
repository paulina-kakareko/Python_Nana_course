def units_multiply(number_and_days_dictionary):
    user_number_of_days = int(number_and_days_dictionary["days"])
    if user_number_of_days > 0:
        if number_and_days_dictionary["unit"] == "hours":
            return f"{user_number_of_days} days are {user_number_of_days * 24} hours"
        elif number_and_days_dictionary["unit"] == "minutes":
            return f"{user_number_of_days} days are {user_number_of_days * 24*60} minutes"
        else:
            return "Unsupported unit"
    elif user_number_of_days == 0:
        return "You entered 0, please enter a valid positive number"


def validate_and_execute(number_and_days_dictionary):
    if number_and_days_dictionary["days"].isdigit():
        my_var = units_multiply(number_and_days_dictionary)
        print(my_var)
    else:
        print("Not valid number of days")