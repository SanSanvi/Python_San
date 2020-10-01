def fib_series(num):
    fib_series = []
    fib_series.append(0)
    fib_series.append(1)

    #first element
    f = 0
    #second element
    s = 1
    for index in range(2,num):
        next = f+s
        fib_series.append(next)
        f = s
        s = next

    print(fib_series)

num = -1
while (num <= 0):
    num = int(input('Please enter the number of fib_series: '))
    if num <=0:
        print('The number entered is invalid. Please enter a positive number greater than 0')

fib_series(num)
