def fibonacciSeries(num):  #user-defined function
    if num <= 1:
        return num
    else:
        return fibonacciSeries(num-1) + fibonacciSeries(num-2)

# take input
num = int(input('Enter number of terms: '))

# print fibonacci series
if num <= 0:
        print('Please enter a positive integer')
else:
    print('The fibonacci series:')
    for i in range(num):
        print(fibonacciSeries(i), end=' ')