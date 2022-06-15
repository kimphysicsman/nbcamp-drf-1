def sum(num1, *args):
    if len(args) != 0:
        return num1 + sum(*args)
    else :
        print('--args example--')
        return num1

print(sum(1, 2, 3, 4, 5, 6, 7))

def print_info(**kwargs):
    print('--kwargs example--')
    if kwargs is not None:
        for item in kwargs.items():
            print(f'{item[0]} is {item[1]}')

print_info(name='dongwoo', year=29, weight=75, height=176)
   
