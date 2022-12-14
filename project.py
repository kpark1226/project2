import csv
from matplotlib import pyplot as plt
# retail = open('Retail_Food_Stores.csv')
# reader = csv.reader(retail)
# data = list(reader)
# data = data[1:]
# square_footage = []
# for i in data:
#     if 200000>=int(i[-2])>20000:
#         square_footage.append(int(i[-2]))
# square_footage.sort()
# plt.hist(square_footage, bins = 20, edgecolor='black')
# plt.xlabel('Square Footage')
# plt.ylabel('Number of Retail Food Stores')
# plt.title('Square Footage of Retail Food Stores in New York')
# plt.show()

import json
pop = open('pop.json')
reader = pop.read()
popjson = json.loads(reader)
popdata = popjson[1]
popdata = popdata[::-1]
year = range(21)
population_early = []
population_late = []
for i in popdata:
    if int(i['date']) <1981:
        population_early.append(i['value'])
    elif 2021>int(i['date']) >=2000:
        population_late.append(i['value'])

plt.title('Population in the United States over 20 years')
plt.plot(year,population_early, label='Population 1960-1980')
plt.plot(year,population_late, label='Population 2000-2020')
plt.xlabel('Years since 1960/2000')
plt.ylabel('Population in Millions')
plt.legend()
plt.show()

    