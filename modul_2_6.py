string = ''
numb = int(input())
if numb <= 2 or numb >= 21:
    print('Введено неккоректное число')
else:
    for i in range(1, numb +1):
        for j in range(i + 1, numb + 1):
            if numb %(j + i) == 0:
                string += str(i) + str(j)
    print(f'{numb} - {string}')





