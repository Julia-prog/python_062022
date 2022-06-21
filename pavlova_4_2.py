'''2. Написать функцию currency_rates(), принимающую в качестве аргумента 
код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты 
по отношению к рублю. '''

import requests
import json

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
dict_json = json.loads(response.text)
def poisk():#Создаем словарь возможных валют
    dict_valute = {}
    for k,v in dict_json['Valute'].items():
        dict_valute[k]=v['Name']
    return dict_valute

def currency_rates(val):
    try:  
        print(f"Курс валюты {dict_json['Valute'][val]['Name']} равен {float(dict_json['Valute'][val]['Value'])}")
    except KeyError:
        dict_valute=poisk()
        print(f'None.выберите валюту из списка доступных валют \n{dict_valute}')
    
   
if __name__== '__main__':

    currency_rates('USD')
    currency_rates('EUR')
    currency_rates('ER')




