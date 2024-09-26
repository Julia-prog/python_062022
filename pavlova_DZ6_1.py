# 1. Получить список кортежей вида: 
#  ('141.138.90.60', 'GET', '/downloads/product_2')

FILENAME = '/Users/julia/Desktop/GB_python1/dz1/nginx_logs.txt'


def parser(data):
    data = data.split('- -')
    result=data[:1]+((''.join(data[1:])).split('"')[1].split(' /'))
    result[-1]='/'+result[-1]
    return result

pars_list=[]

with open(FILENAME,'r',encoding='utf_8') as f:
    for line in f:
        pars_list.append(tuple(parser(line)))

print(pars_list[:5])



       
        