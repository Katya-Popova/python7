def read_database():
    db_list =[]
    db_file=open("database.txt", "r", encoding='utf-8')
    lineList = db_file.readlines()
    for line in lineList:
        if line != "":
            db_list.append(line.replace("\n", "").split(" "))
    db_file.close()
    return db_list

def rewrite_database(data):
    db_file = open("database.txt", "w",encoding='utf-8')
    for line in data:
        db_file.write(" ".join(line)+'\n')
    db_file.close()

def input_data_local(data):
    data_second_name = input("Введите фамилию пользователя: ").strip()
    if data_second_name =="":
        data_second_name="_"
    data_first_name = input("Введите имя пользователя: ").strip()
    if data_first_name =="":
        data_first_name="_"
    data_father_name = input("Введите отчество пользователя: ").strip()
    if data_father_name =="":
        data_father_name="_"
    phone_numbers = input("Введите телефон пользователя: ").strip()
    if phone_numbers =="":
        phone_numbers="_"
    line = (data_second_name, data_first_name, data_father_name, phone_numbers)
    data.append(line)
    rewrite_database(data)
    
def find_data_local(data):
    flag=0
    search_atribut = input("Введите Фаилию или Имя: ")
    for line in data:
        for user_atribut in line:
            if user_atribut== search_atribut:
                print("\nФамилия: ", line[0], "\nИмя: ", line[1], "\nОтчество: ",line[2],"\nНомер телефона: ", line[3])
                flag=1
    if flag==0:
        print('\nТакой записи нет')

def export_data(data):
    with open('exporter.csv',"w",encoding='utf-8') as file1:
        file1.write("Фамилия;Имя;Отчество;Номер телефона\n")
        for line in data:
            for atribute in range(len(line)-1):
                file1.write(line[atribute]+";")
            file1.write(line[atribute+1]+"\n")

def import_data(data):
    path = input('Введите имя файла для импорта: ')
    with open(path, "r", encoding='utf-8') as file:
        linelist= file.readlines()
        for line in linelist:
            if line !='':
                line1 =line.replace(' ',';')
                line2 =line1.replace(',',';')
                line3 =line2.replace('.',';')
                data.append(line3.replace('\n', '').split(';'))
    rewrite_database(data)

def print_data(data):
    print(data)





