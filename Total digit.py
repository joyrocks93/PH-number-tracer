'''
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
'''
a=int(input("Enter a number:"))
c=0
while(a>0):
    a=a//10
    c+=1
print(c)
    
