def rec_fib_series(num):
    if num <=1:
        return num
    else:
        return rec_fib_series(num-1)+rec_fib_series(num-2)


num = -1
while (num <= 0):
    num = int(input('Please enter the number of fib_series: '))
    if num <=0:
        print('The number entered is invalid. Please enter a positive number greater than 0')

for index in range(num):
    print(rec_fib_series(index), end = ' ')
