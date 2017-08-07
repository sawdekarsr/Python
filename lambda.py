#####################Simple lambda function#####################
f = lambda x,y:x*y        #Lambda function for multiplication
print f(4,5)              #Call lambda function

#####################List comprehension#####################
numberList = [i+1 for i in range(10)]    #List comprehension
print numberList

#####################Using lamda function in list comprehension#####################
fsquare = lambda x:x*x          #Lambda fuction to calculate square of a number
squareList = [fsquare(i) for i in numberList]     #Use lambda function in list comprehension
print squareList

#####################Use filter fuction along with lambda#####################
print filter(lambda i: i>10 and i<60, squareList)  #Use filter() to get numbers in between 10 and 60 from the square of numbers

#####################Write above code in different style. Syntax : filter(function, list)#####################
ffilterLambda = lambda i: i>10 and i<60          #First define lambda function with filter conditions
print filter(ffilterLambda, squareList)          #call filter() by passing 1st argument as lambda function and second as data.
