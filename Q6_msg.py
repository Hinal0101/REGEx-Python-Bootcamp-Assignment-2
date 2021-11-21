# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

#  Q6.You have to run your program at 12:00am, Date: 20th November, 2021 and wish your friend a “Happy 
#     Birthday” through your whatsApp.
#     HINT
#     You can use Datetime module or time module and web browser for the same
#     Use of List
#     Use of conditional statements and loops.


from datetime import date
today=date.today()
my_birthday=date(today.year,11,21)
if my_birthday==today:
    print("Hii.. Happy Birthday !!")
