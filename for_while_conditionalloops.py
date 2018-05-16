#loops and iterations
#for loops and while loops

nums = [1, 2 ,3, 4, 5] #list of numbers

# for num in nums:
#     print(num)

#let's say we need a certain number in the list and
#stop looking when you've found the value

#
# for num in nums:
#     if num == 3:
#         print('Found!')
#         break
#     print(num)


#use the continue clause to continue printing after the found clause
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)


#Nested loops
#beware using nested loops
# for num in nums:
#     for letter in 'abc':
#         print(num,letter)


#built in function called Range()
#to run through a loop X times
# for i in range(10):
#     print(i)


#print numbers 1 to 10
# for i in range(1,11):
#     print(i)


#While loops


#print x=0 to 9
x =0

while x <10:
    if (x == 5):
        break
    print(x)
    x += 1
