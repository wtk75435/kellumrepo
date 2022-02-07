#Reading lines from a file and converting strings
# #User Input and While loop

file_handle=open("classread.txt") #open file
#open(file pathway) ##if file is in same folder no need ###creates file object if correct
file_lines=file_handle.readlines() #read the opened file line by line
print(file_lines) #show what is opended
file_numbers=[int(line) for line in file_lines]
file_numbers=[int(line)**2 for line in file_lines if int(line) >5]
print (file_numbers)
file_handle.close() #close file

#same thing with for loop
file_handle=open("classread.txt")
file_lines=file_handle.readlines()
file_numbers=[]
for line in file_lines:
    num=int(line)
    if num>5:
        file_numbers.append(num**2)
print(file_numbers)
print(file_numbers)
file_handle.close() #close file

file_handle=open("classread.txt")
file_numbers=[]

while True: #continue loop until break ##if no false statment is located. it will wait for more code
    line =file_handle.readline()
    if line == "": break #
    num=int(line)
    if num>5:
        file_numbers.append(num**2)
file_handle.close()

#user input
while True:
    user_input=input("guess a number")
    if user_input=="q":
        print("goodbyte")
        break
    print("your input was", user_input, "guess again. input q to leave")

