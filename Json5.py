import json
from urllib.request import urlopen


with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as response:
    sourse = response.read() #считываем данные с внешнего ресурса
data = json.loads(sourse) #преобразовали строку в словарь
print("Курс доллара: {}".format(data['Valute']['USD']['Value']))
print("Курс евро: {}".format(data['Valute']['EUR']['Value']))

print(data)
dif = data['Valute']['EUR']['Value'] - data['Valute']['USD']['Value']
dif2 = 1
print(data['Valute']['EUR']['Name'], "больше", data['Valute']['USD']['Name'], "на", round(dif,2))
if data['Valute']['EUR']['Value'] > data['Valute']['USD']['Value']:
    dif2 = data['Valute']['EUR']['Value']/data['Valute']['USD']['Value']
    print(data['Valute']['EUR']['Name'], "больше", data['Valute']['USD']['Name'], "в", round(dif2,2))
else:
    dif2 = data['Valute']['USD']['Value'] / data['Valute']['EUR']['Value']
    print(data['Valute']['USD']['Name'], "больше", data['Valute']['EUR']['Name'], "в", round(dif2,2))




