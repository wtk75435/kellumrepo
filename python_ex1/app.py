from bitarray import test


print("Go Dawgs")
the_score=33.18 #using underscores are refered to as snake lettering
print(the_score) # comment symbol
"comment symbols"
test_list=[1,2,3,5,4,6]

#for loop examples
for i in range (0, len(test_list)) :
    print(i, test_list[i])

for item in test_list:
    print(item)

for index in range(0,len(test_list)):
    print(test_list[index])
'''
block 
comment
'''
#sampling a list
print(test_list)#whole list
print(test_list[3]) #single entry
print(test_list[3:4]) #includes item 3 not 4. same as before
print(test_list[2:5]) #includes item 2,3,4 but not 5
print(test_list[:3]) #print first 3 items in list
print(test_list[-1])#-1 is ref to the last item
print(test_list[::-1]) #access the lsit in reverse
print(reversed(test_list)) #print reverser of tst list
# that gives <list_reverseiterator object at 0x7fa7c4556fd0>
print(list(reversed(test_list)))

anthr_list=test_list.copy() #copy() creates a different location for the list memory
#if no copy() is made, the original will be altered
anthr_list[3]=18 #changes item [3] to 18 in 'another_list'
print(test_list)

anthr2_list=anthr_list
print(id(anthr_list),id(anthr2_list)) #prints address of info in python memory
print(list(sorted(test_list)))
anthr_list.sort() #sort() changes memory
anthr2_list.sort(reverse=True)
print(anthr_list) #memory is now sorted

print(anthr2_list)
numbers=[]
for i in range(0,11):
    numbers.append(i)

print(numbers)

for i in range(0,11):
    numbers[i]=numbers[i]**2
print(numbers)

