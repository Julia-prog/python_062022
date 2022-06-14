# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
#  а в другом — данные об их хобби.  Написать код, 
# загружающий данные из обоих файлов и формирующий из них словарь:
#  ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. 
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта 
# с кодом «1». 

import json
# создаем данные
with open('users.csv',"w", encoding='utf-8') as f:
    f.writelines(['Иванов,Иван,Иванович \n','Петров,Петр,Петрович\n','Сидоров,Сидор,Сидорович'])
    

with open('hobby.csv',"w", encoding='utf-8') as f:
    f.writelines(['скалолазание,охота\n','горные лыжи\n'])


# считываем данные
with open('users.csv',"r", encoding='utf-8') as f_us:
    with open('hobby.csv',"r", encoding='utf-8') as f_ho:
        # словать с результатом решения
        users_dict={} 

        index=0
        users={}
        for line in f_us:
            users[index]=line.replace(',',' ')
            index+=1

        index=0
        hobby={}
        for line in f_ho:
            hobby[index]=line.replace(',',' ')
            try:
                users_dict[users[index]]=hobby[index] #проверка 
            except KeyError:
                print(exit(1))

            index+=1

        if users[index]:
            users_dict[users[index]]=None




with open('DZ1_3_result.json',"w", encoding='utf-8') as f:
    json.dump(users_dict, f,indent=4)

with open('DZ1result.json',"r", encoding='utf-8') as f:
    print(json.load(f))


        
            






