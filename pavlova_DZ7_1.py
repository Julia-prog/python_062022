#  Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


import shutil
import os
from pathlib import Path

dir_ = os.path.abspath(os.curdir)

structure={'my_project':['settings','mainapp','adminapp','authapp']}

for k,v in structure.items():
    
    for el in v:
        p = Path(f'{dir_}/{k}/{el}')
        p.mkdir(parents=True, exist_ok=True)


# shutil.rmtree('my_project')    
  
# чтобы расширить продолжаем словарь structure={..:.., 'my_project/settings':'mainapp'}
  

