#####################Simple lambda function#####################
f = lambda x,y:x*y        #Lambda function for multiplication
print("Multification of 4 & 5 using lambda() : {}".format(f(4,5)))    #20

#####################List comprehension#####################
numberList = [i+1 for i in range(10)]    #List comprehension                     #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers from 1 to 10 using list comprehension : {}".format(numberList))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#####################Using lamda function in list comprehension#####################
fsquare = lambda x:x*x          #Lambda fuction to calculate square of a number
squareList = [fsquare(i) for i in numberList]     #Use lambda function in list comprehension
print("Squares of all numbers from 1 to 10 using lamda and list comprehension :  {}".format(squareList))      #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#####################Use filter fuction along with lambda#####################
#Use filter() to get numbers in between 10 and 60 from the square of numbers
print("Print squares numbers between 10 to 60 : {}".format(filter(lambda i: i>10 and i<60, squareList)))      #[16, 25, 36, 49]

#####################Write above code in different style. Syntax : filter(function, list)#####################
#call filter() by passing 1st argument as lambda function and second as data.
ffilterLambda = lambda i: i>10 and i<60          #First define lambda function with filter conditions
print("Print squares numbers between 10 to 60 by calling lambda() inside filter() : {}".format(filter(ffilterLambda, squareList)))     #[16, 25, 36, 49]

#####################map() with lambda#####################
#Define lambda function inside map()
print("Squares of all numbers from 1 to 10 using map() : {}".format(map(lambda i:i*i, numberList)))                              #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Call exisiting lambda() instead of defining in map()
print("Squares of all numbers from 1 to 10 using calling existing lambda() inside map() : {}".format(map(fsquare, squareList)))  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

firstList  = [(i+1)*10 for i in range(10)]      #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
secondList = [(i+1)*100 for i in range(10)]     #[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
thirdList  = [(i+1)*1000 for i in range(10)]    #[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
print("Addition of elements sharing same index from all arrays {}".format(map(lambda x, y, z: x+y+z, firstList, secondList, thirdList)))  #[1110, 2220, 3330, 4440, 5550, 6660, 7770, 8880, 9990, 11100]
