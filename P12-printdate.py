from datetime import*

# The now method returns the current date and time
# The strftime method allows you to format the date 
# These methods can not be added together simultaneously... I think
# You have to create a variable that stores the method that gives the current date
# You then apply the method that allows you to format the date to that variable


curr_datetime = datetime.now()
format_date = curr_datetime.strftime("%d/%m/%Y")
print("Current Date = {}".format(format_date))
