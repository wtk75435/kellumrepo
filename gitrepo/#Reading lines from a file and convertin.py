#Reading lines from a file and converting strings
# #User Input and While loop
file_handle=open("classread.txt")
#open(file pathway) ##if file is in same folder no need ###creates file object if correct
file_lines=file_handle.readline()
print(file_lines)

file_handle.close() #close for later use