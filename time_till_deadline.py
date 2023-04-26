from datetime import datetime


user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

# calculate how many days from now till deadline
time_till_deadline = deadline_date - today_date
print(f"Dear User! Time remaining for your goal: {goal} is {time_till_deadline.days} days")
