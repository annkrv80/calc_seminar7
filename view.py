def show_menu():
    print('1-Калькулятор')
    print('2-Конвертер')
    return input('Введите цифрy: ')

def show_calc_enter():
    return input ('Введите выражение: ')

def show_convert_enter():
    return input ('Введите количество килограмм: ')

def show_calc_res(res):
    print('Результат =' + str(res))

def show_convert_res(res):
    print(f'{res[0]} Кг = {res[1]} Гр')