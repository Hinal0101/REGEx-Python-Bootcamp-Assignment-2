# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

# Q3. You need a create a function which will check the validation of user password
#       - Conditions are
#       - password should have at least 1 capital letter
#       - 1 smaller letter
#       - Any special character only like !@#$%^
#       - Length of the password should be minimum 6 character & maximum 15 character
#       - Print a suitable message in case all the conditions are true other any other message


def validate_password(user_input):
    a=b=c=-1
    if len(user_input)>=6 and len(user_input)<=15:
        for i in user_input:
            if i>="A" and i<="Z":
                a+=1
            if i>="a" and i<="z":
                b+=1
            if i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^":
                c+=1
            
        if a>=0 and b>=0 and c>=0:
            print("Password Saved Successfully !!!")
        else:
            if a<0:
                print("Should contain atleast one capital letter")
            if b<0:
                print("Should contain atleast one small letter")
            if c<0:
                print("Should contain atleast one special character")
    else:
        print("Length should be minimum 6 and maximum 15")



print("Enter Password")
user_input=input()
validate_password(user_input)