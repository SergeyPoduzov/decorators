# задача 2
# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции,
# аргументы, с которыми вызвалась и возвращаемое значение.
# Написать декоратор из п.1, но с параметром – путь к логам.


from datetime import datetime
import math

def path_loging_function(file_path):
    def logging_function(foo):
        def new_foo(*args, **kwargss):
            result = foo(*args, **kwargss)


            log = ''
            log += f'\n дату и время вызова функции : {datetime.now()}'
            log += f'\n\t имя функции {foo.__name__} c с аргументами: {args}, {kwargss}  '
            log += f'\n\tРезультат выполнения: {result}'


            print(log)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f"{log}\n")

            return result

        return new_foo
    return logging_function

@path_loging_function('log_square_paralellipipid.txt')
def square_paralellipipid(a,b, x):
    """Вычисляем площадь папалелилипида - одна сторона на ругую на sin угла"""
    # конвертировать из градусов в радианы
    n_rad = x * math.pi / 180
    return a*b*math.sin(n_rad)


square_paralellipipid(5,3,30)
