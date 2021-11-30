# Цей міні-проєкт я розробив, надихаючись цим проєктом з Текстів:
# https://texty.org.ua/d/2018/streets/

# Як бачу, мої результати дещо відрізняються від аналогічних результатів Текстів.
# Мабуть, це через те, що я рахував - вулиці, проспекти, провулки та ін.,
# а Тексти - тільки вулиці.

# Data sources:
# post_indexs_10-09-2018.csv

# Що нас цікавить:
    # Назва області"
	# Назва району
	# Назва населеного пункту (повна)
	        # Поштовий індекс населеного пункту
	# Назва вулиці

	# З цих даних можна дізнатись такі цікаві речі:
	# - 10 найпоширеніших назв вулиць по всій Україні,
	# - 10 найпоширеніших назв вулиць - по кожній області України,
	# - 10 найпоширеніших назв вулиць - по кожному району України,

# 1) Завантажуємо файл:
# ...
# на диск

# 2) Читаємо перші 5 стовпчиків, окрім четвертого

import csv
import json

def read_csv_file(name_file_csv):
    with open('post_indexs_10-09-2018.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        # Витягнемо назви усіх вулиць...
        str_list_streets_to_txt_file= ''

        for row in csv_reader:
            if line_count >= 2:
                tmp = row[0].split(';')
                street = ''
                    
                if tmp[2][-2:] == '(0':
                    street = row[1].split(';')
                    street = street[2]
                    str_list_streets_to_txt_file = str_list_streets_to_txt_file + street + '\n'
                else:
                    street = row[0].split(';')
                    street = street[4]
                    str_list_streets_to_txt_file = str_list_streets_to_txt_file + street + '\n'

                line_count += 1

        # print(f'Загалом - {line_count} вулиць в Україні.')
        return str_list_streets_to_txt_file, line_count

def save_name_streets_to_txt_file(name_file_txt, str_list_streets_to_txt_file):
    # ... та, збережемо усі ці назви (вулиць) до txt-файлу
    with open('name_streets_10-09-2018.txt', 'at') as txt_file:
        txt_file.write(str_list_streets_to_txt_file)


# 10 найпоширеніших назв вулиць по всій Україні
    # print('Назви вулиць')

    # set_name_streets = set()
    # line_count = 0

    # for row in csv_reader:
            
    #     if line_count >= 2:
    #         # tmp = row[0].split(';')[4]
    #         tmp = row[0].split(';')
    #         # tmp = tmp[4]
    #         # print(f'{tmp[4]}')
    #         set_name_streets.add(tmp[4])
        
    #     line_count += 1

    #     # print(f'{line_count}')
    
    # # for set_name in set_name_streets:
    # #     print(f'set_name = {set_name}')

    # print(f'Загалом - {len(set_name_streets)} різних назв вулиць в Україні.')


    # Витягнемо назви усіх вулиць...
def get_all_names_streets_csv_file(name_file_csv):
    with open('post_indexs_10-09-2018.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        str_list_streets_to_txt_file= ''
        
        for row in csv_reader:
            if line_count >= 2:
                tmp = row[0].split(';')
                street = ''
                    
                if tmp[2][-2:] == '(0':
                    street = row[1].split(';')
                    street = street[2]
                    str_list_streets_to_txt_file = str_list_streets_to_txt_file + street + '\n'
                else:
                    street = row[0].split(';')
                    street = street[4]
                    str_list_streets_to_txt_file = str_list_streets_to_txt_file + street + '\n'

                line_count += 1

    print(f'Загалом - {line_count} вулиць в Україні.')


# ... та, збережемо усі ці назви (вулиць) до txt-файлу
def save_all_names_streets_to_txt_file(name_file_txt, str_list_streets_to_txt_file):
    with open('name_streets_10-09-2018.txt', 'at') as txt_file:
        txt_file.write(str_list_streets_to_txt_file)


# Створимо множину назв вулиць (без повторень),..
def create_set_name_streets(txt_file_out, txt_file_in):
    set_name_streets = set()

    # ... та витягнемо їх з файлу
    with open(txt_file_out) as txt_file:
        txt_reader = txt_file.readlines()

        for row in txt_reader:
            set_name_streets.add(row)
        
    print(f'Загалом - {len(set_name_streets)} різних назв вулиць в Україні.')

    # print(set_name_streets)
    for unic_name_streets in set_name_streets:
        print(unic_name_streets)

    # ... зберігши до іншого файлу 
    with open(txt_file_in, 'at') as txt_file:
        txt_file.write(str(set_name_streets))

    # print(f'Зберегли')



# Приклад коду для подальшої ф-ції:
# newDict = {}

# 	for word in newListText:
# 		# Створюємо словник частот слів
# 		if word not in newDict:
# 			newDict[word] = 1
# 		elif word in newDict:
# 			newDict[word] = newDict.get(word, 0) + 1

# Створимо словник, ключами якого будуть назви вулиць, а значеннями - їх частоти в даному статист. ряду
def create_dict_name_streets(txt_file_out):
    dict_name_streets = {}

    # витягнемо з файлу назви вулиць...
    with open(txt_file_out) as txt_file:
        txt_reader = txt_file.readlines()

        for row in txt_reader:
            row = row[:-2]                      # for deleting '\n'
            if row not in dict_name_streets:
                dict_name_streets[row] = 1
            else:
                dict_name_streets[row] = dict_name_streets.get(row, 0) + 1

    return dict_name_streets


# Сортування словника, та запис його до файлу
def sortedDict(dictionary):
	newSortedDict =  sorted(dictionary.items(), key = lambda kv:(kv[1], kv[0]))

	return newSortedDict


# ... зберігши до іншого файлу 
def save_dict_to_json_file(dict_val, json_file_in):
    with open(json_file_in, "a", encoding="utf8") as write_file:
        json.dump(dict_val, write_file, indent=4, ensure_ascii=False)


def main():
    # txt_file_out = 'name_streets_10-09-2018.txt'
    # txt_file_in = 'unical_name_streets_10-09-2018.txt'

    # create_set_name_streets(txt_file_out, txt_file_in)

    txt_file_out = 'name_streets_10-09-2018.txt'
    # json_file_in = 'dict_name_streets_10-09-2018.json'
    json_sort_dict_file_in = 'sort_dict_name_streets_10-09-2018.json'

    dict_name_streets = create_dict_name_streets(txt_file_out)

    sort_dict_name_streets = sortedDict(dict_name_streets)

    print(len(sort_dict_name_streets))

    # save_dict_to_json_file(sort_dict_name_streets, json_sort_dict_file_in)


if __name__ == "__main__":
    main()