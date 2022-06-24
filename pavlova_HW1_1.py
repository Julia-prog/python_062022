'''1. Реализовать вывод информации о промежутке времени в зависимости
 от его продолжительности duration в секундах: 
до минуты: <s> сек;
до часа: <m> мин <s> сек; 
до суток: <h> час <m> мин <s> сек; 
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек'''

duration = [53,153,4153,400153]
def dur_pri(duration):
    # до минуты
    if 0 <= duration < 60: 
        print(f'{duration} сек')
    # до часа
    elif 60 <= duration < 60*60:
        print(f'{duration//60} мин {duration%60} сек')
    # до суток
    elif 60*60 <= duration < 60*60*24:
        print(f'{duration//(60*60)} час {duration//60%60} мин {duration%60} сек')
    # остальные
    elif 60*60*24 <= duration:
        print(f'{duration//(60*60*24)} дн {duration%(60*60*24)//(60*60)} час {duration//60%60} мин {duration%60} сек')


for el in duration:
    dur_pri(el)


