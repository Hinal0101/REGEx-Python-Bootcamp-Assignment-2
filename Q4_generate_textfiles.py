# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

# Q4. Write a Python Program to generate 26 text files named A.txt, B.txt and so on up to Z.txt


def generate_text_files():
    for i in range(65,91):
        file=str(chr(i))+".txt"
        print
        with open(file,"x") as fileObj:
            fileObj.close()



generate_text_files()
