#This file allows us to import the txt file and use it when writing code
log_file = open("um-server-01.txt")


#The below function is reading the txt file we imported above and checking to see if the day is equal to Tue. It will then print all the lines in the imported file that have tuesday as the day.
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


#this line is calling the function written above.
sales_reports(log_file)
