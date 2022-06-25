''' Написать функцию num_translate(), переводящую 
числительные от 0 до 10 c английского на русский язык. Например:
>>> num_translate("one")
"один"
Если перевод сделать невозможно, вернуть None. '''

def num_translate(name):
    dir_trans = {
        'one':'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять'         
    }
    print(dir_trans.get(name))


num_translate("one")
num_translate("eight")
num_translate('l')

