'''
#    Погружение в Python (семинары)
##   Урок 10. ООП. Начало

###  Задание № 7
Решить задачи, которые не успели решить на семинаре.
*Доработаем задачи 5-6*. Создайте класс-фабрику. 
○ Класс принимает тип животного (название одного из созданных классов) 
и параметры для этого типа. 
○ Внутри класса создайте экземпляр на основе переданного типа и 
верните его из класса-фабрики.
Возьмите любые задачи из прошлых семинаров 
(*например сериализация данных*), которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. 
*Задачи должны решаться через вызов методов* 
'''
import csv
import json
from pathlib import Path
import pickle


class Serialization:
    def __init__(self, directory: Path):
        self.directory = directory

    def serialization_files(self):
        data = {}
        for i in self.directory.rglob('*'):
            size = 0
            if i.is_dir():
                for file in i.rglob('*'):
                    size += file.stat().st_size
            else:
                size = i.stat().st_size

            data[i.name] = {
                'parent': i.parent.name,
                'type': 'directory' if i.is_dir() else 'file',
                'size': size
            }

        with open(Path(self.directory, 'json_data.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        with open(Path(self.directory, 'pickle_data.pickle'), 'wb') as f:
            pickle.dump(data, f)

        with open(Path(self.directory, 'csv_data.csv'), 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            header = ['file', 'parent', 'type', 'size']
            csv_writer.writerow(header)

            for key, value in data.items():
                line = [key]
                values = [val for val in value.values()]
                line.extend(values)
                csv_writer.writerow(line)


if __name__ == '__main__':
    s = Serialization(Path('/Users/'))
    s.serialization_files()