"""1. Написать функцию email_parse(<email_address>), 
которая при помощи регулярного выражения извлекает имя 
пользователя и почтовый домен из email адреса и возвращает 
их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. 
Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru"""


import re

def valid(func):
    def wrap(arg):
        PARS=re.compile(r'([a-zA_Z0-9_]+)@([a-zA_Z0-9_]+)\.([a-zA_Z0-9_]+)')
        if  PARS.match(arg):
            markup=func(arg)
            return markup
        else:
            raise ValueError(f'wrong email: {arg}')
    return wrap


@valid
def email_parse(email_address):
    RE_GET_PARSER_ = re.compile(r'(?P<key>.+)@(?P<val>.+\b)')
    print(*map(lambda x: x.groupdict(), RE_GET_PARSER_.finditer(email_address)), sep=', ')

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
