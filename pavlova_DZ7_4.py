'''4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
 в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
  а значения — общее количество файлов (в том числе и в подпапках),
   размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.'''


import os, shutil
import random

dir_= os.path.abspath(os.curdir)
folder = os.path.join(dir_,'some_data')


def some_data():
  os.mkdir(folder)
  letters = [chr(code) for code in range(ord('a'), ord('z') + 1)] 
  for _ in range(10 ** 3):
      f_name = ''.join(random.sample(letters, random.randint(5, 10))) 
      f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5))) 
      with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)
# some_data()
# shutil.rmtree(folder)

result={
        100:0,
        1000:0,
        10000:0,
        100000:0
        }

def size_files(folder):
  for file in os.listdir(folder):
    size=os.stat(os.path.join(folder,file)).st_size
    
    min_size=0
    for i in range(2,6):
      max_size=10**i
      if size in range(min_size,max_size):
        result[max_size]+=1
        min_size=max_size


size_files(folder)
print(result)


    

