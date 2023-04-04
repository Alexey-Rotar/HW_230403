def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])

def show_item(filename, ID):
    data_array = read_file(filename)
    print(data_array[ID])

def find_item_ID(filename, ID):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        if data_array[i][0] == str(ID):
            return i
        else:
            return None      

def change_item(filename, item_ID):
    data_array = read_file(filename)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    data_array[item_ID][1] = lastname
    data_array[item_ID][2] = firstname
    data_array[item_ID][3] = secondname
    data_array[item_ID][4] = phone
    write_file(filename, data_array)
    print('Измененная запись: ')
    print(data_array[item_ID])

def delete_item(filename, ID):
    data_array = read_file(filename)
    data_array.pop(int(ID))
    write_file(filename, data_array)

def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        user_operation = int(input('Укажите ID записи для внесения изменений: '))
        ID = find_item_ID(filename, user_operation)
        if ID != None and ID != 0:
            print('Будут вноситься изменения в запись: ')
            show_item(filename, ID)
            change_item(filename, ID)
        else:
            print('Запись с таким ID не найдена!')
    elif user_operation == 4:
        user_operation = int(input('Укажите ID записи для удаления: '))
        ID = find_item_ID(filename, user_operation)
        if ID != None and ID != 0:
            print('Удалена запись: ')
            show_item(filename, ID)
            delete_item(filename, ID)
        else:
            print('Запись с таким ID не найдена!')

filename = 'file.txt'
menu()