# Задача 3
# Применить написанный логгер к приложению из любого предыдущего д/з.

import requests
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

class Downloader:

    def __init__(self):
        pass


    def __iter__(self):
        return self

    @logging_function
    def __next__(self):

        if self.start < self.end:
            self.start += 1
            self.content = self.res[self.start]
            self.txt = ''
            self.txt += self.content['name']['common']

            self.txt += ' - '
            try:
                self.txt += self.content['tld'][0]
            except:
                self.txt += 'none'
            self.txt +='\n'
            return self.txt


        else:
            self.start = -1
            raise StopIteration


    def download(self, url, file_path):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Wrong status code")
        self.res = response.json()
        self.start = -1
        self.end = len(self.res) - 1
        with open(file_path, 'w', encoding='utf-8') as file:
            for chunk in self:
                file.write(chunk)

    def printing(self):
        print("Все страны из класса: ")
        for chunk in self:
            print(chunk)

downloader = Downloader()

downloader.download('https://raw.githubusercontent.com/mledoze/countries/master/countries.json', 'count7.txt')
downloader.printing()