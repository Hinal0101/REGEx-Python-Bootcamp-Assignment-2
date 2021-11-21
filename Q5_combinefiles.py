# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

#  Q5.Write a Python program to combine each line from the first file with the corresponding line in the 
#     second file and save it into the Third file.

with open('Q5_file1.txt') as f1,open('Q5_file2.txt') as f2:
	for l1,l2 in zip(f1,f2):
            with open("Q5_file3_combine.txt","a") as fileObj:
                fileObj.writelines(l1+l2)
fileObj.close()