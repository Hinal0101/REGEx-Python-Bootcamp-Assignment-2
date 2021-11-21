# REGEx Python Bootcamp
# Name : Jethava Hinal Manojkumar 
# Task 2

# Q2. Open a file in a read & write format make sure you make the write process from the byte position of 
#     your pointer from 15
#     - validate that by going through the file again


fileObj=open("Q2_data.txt","r")

output=fileObj.read(15)

print("Pointer is at byte",fileObj.tell())
print(output)
fileObj.close()