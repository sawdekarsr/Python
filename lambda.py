f = lambda x,y:x*y        #Lambda function for multiplication
print f(4,5)              #Call lambda function

a = [i+1 for i in range(10)]    #List comprehension
print a

fsquare = lambda x:x*x          #Lambda fuction to calculate square of a number
b = [fsquare(i) for i in a]     #Use lambda function in list comprehension
print b
