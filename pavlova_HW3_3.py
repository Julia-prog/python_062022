'''Написать функцию thesaurus(), 
принимающую в качестве аргументов имена сотрудников и
 возвращающую словарь, в котором ключи — первые буквы имён,
  а значения — списки, содержащие имена, начинающиеся с 
  соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}'''
def thesaurus(*args):
    dict_names = {}
    
    for el in args:
        if dict_names.get(el[0]) ==None:
            dict_names.setdefault(el[0],[el])
        else:
            dict_names[el[0]].append(el)

    for k,v in dict_names.items():
        print(f'{k} : {v}')


thesaurus("Иван", "Мария", "Петр", "Илья")

