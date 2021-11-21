# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

# Q1. You need to take two input as number from the user and find out the Greatest Common Divisor of
#     those two number and save it in a C drive with the file name as gcd_data.txt



def gcd(a, b):
      
    if (a == 0):
        return b
    if (b == 0):
        return a
  
    if (a == b):
        return a
  
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
  
print("Enter the 1st number")
a=int(input())
print("Enter the 2nd number")
b=int(input())
result=gcd(a,b)



string="The gcd of two numbers is "+str(result)
with open("gcd_data.txt","x") as fileObj:
    fileObj.write(string)
    fileObj.close()
