"""|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html"""

import shutil
import os
from pathlib import Path


# создаем структуру
dir_ = os.path.abspath(os.curdir)
structure = {'my_project':['settings','mainapp','authapp'],
                'my_project/settings':['__init__.py','dev.py','prod.py'],
                'my_project/mainapp':['__init__.py','models.py','views.py','templates'],
                'my_project/mainapp/templates':['mainapp'],
                 'my_project/mainapp/templates/mainapp':['base.html','index.html'],
                'my_project/authapp':['__init__.py','models.py','views.py','templates'],
                'my_project/authapp/templates':['authapp'],
                'my_project/authapp/templates/authapp':['base.html','index.html']
                }


def valid(name):
    if '.' in name:
        return False
    else:
        return True


for k,v in structure.items():
    for el in v:
        if valid(el):
            p = Path(f'{dir_}/{k}/{el}')
            p.mkdir(parents=True, exist_ok=True)
        else:
            folder=k
            with open(os.path.join( f'{k}', f'{el}'), 'wb') as f:
                pass


folder=os.path.join(f'{dir_}','my_project')
new_path=os.path.join( dir_, 'templates')
os.mkdir(new_path)
for path, dir, files in os.walk(folder):
    for file in files:
        if file.lower().endswith('.html'):
            new_path_2=os.path.join(new_path,path.split('/')[-1])
            try:
                os.mkdir(new_path_2)
            except FileExistsError:
                pass
            shutil.copyfile(os.path.join(f'{path}',f'{file}'), os.path.join(f'{new_path_2}',f'{file}'))

# shutil.rmtree('my_project')   
# shutil.rmtree('templates')   

