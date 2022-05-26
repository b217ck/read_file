#подключение модулей
import os
import re
from collections import Counter

#показать текущую директорию
print('Текущая директория:', os.getcwd())

#показать все файлы и папки в текущем каталоге
print("Все папки и файлы в текущей директории:", os.listdir())

#ввод имени файла пользователей
print('Введите имя файла в текущем каталоге из списка выше:')
srcfile = str(input())

#показать содержимое файла
with open(srcfile, encoding="utf8") as myFile:
    open_file = myFile.read()
    print('Содержимое файла:', open_file)

#найти все слова в файле
words = re.findall(r'\w+', open_file)
#print('Слова:', words)

#найти слова больше 3 символов
words_3 = ''
for (index, elem) in enumerate(words):
    if len(elem) > 3:
        words_3 += ''.join(words[index]) + ','
        #print('Больше 3 символов:', elem)

#посчитать повторы слов больше 3 символов
word_counts_split = re.split(',', words_3)
word_counts_3 = Counter(word_counts_split)
#print('Повторы слов:', word_counts_3)

#функция проверки слова на английский алфавит
def match(text, alpha=set('abcdefghijklmnopqrstuvwxyz')):
    return alpha.isdisjoint(text.lower())

#найти английские слова
words_en = ''
for (index, elem) in enumerate(words):
    if match(elem) == False:
        words_en += ''.join(words[index]) + ', '
        #print('Английские слова:', elem)

#найти самое длинное слово на английском
words_en_split = re.split(',', words_en)
longest = max(words_en_split, key=len)

#результаты
print('Наиболее часто встречающееся слово из тех, что имеют размер более 3 символов:', word_counts_3.most_common(1) )
print('Наиболее длинное слово на английском языке:', longest)
