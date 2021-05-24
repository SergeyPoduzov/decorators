 # Задача 1
# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции,
# аргументы, с которыми вызвалась и возвращаемое значение.

from datetime import datetime


def logging_function(foo):
    def new_foo(*args, **kwargss):
        result = foo(*args, **kwargss)


        log = ''
        log += f'\n дату и время вызова функции : {datetime.now()}'
        log += f'\n\t имя функции {foo.__name__} c с аргументами: {args}, {kwargss}  '
        log += f'\n\tРезультат выполнения: {result}'


        print(log)
        with open('log_list.txt', 'a', encoding='utf-8') as f:
            f.write(f"{log}\n")

        return result

    return new_foo

@logging_function
def square_triaangle(a,b):
    """Вычисляем площадь прямоугольнго треугольника"""
    return a*b/2


square_triaangle(5,3)
