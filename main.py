import pandas as pd

data = pd.read_excel('data.xls')
data = data.values.tolist()


data_2017 = []
jumlah_harga = 0
euler = 2.71828
x=1
for i in data:
  data_2017.append([i[0],i[1]])

for i in data_2017:
  jumlah_harga += i[1]

x = 1
delta = jumlah_harga/34

probabilitas_2017 =  ( delta**(x) )   / x
print("probabilitas 2017 =","2.7182 **",delta,"*",probabilitas_2017)


data_2018 = []
jumlah_harga = 0
euler = 2.71828
x=1
for i in data:
  data_2018.append([i[0],i[2]])

for i in data_2018:
  jumlah_harga += i[1]

x = 1
delta = jumlah_harga/34

probabilitas_2018 =  ( delta**(x) )   / x
print("probabilitas 2018 =","2.7182 **",delta,"*",probabilitas_2018)


data_2019 = []
jumlah_harga = 0
euler = 2.71828
x=1
for i in data:
  data_2019.append([i[0],i[3]])

for i in data_2019:
  jumlah_harga += i[1]

x = 1
delta = jumlah_harga/34

probabilitas_2019 =  ( delta**(x) )   / x
print("probabilitas 2019 =","2.7182 **",delta,"*",probabilitas_2019)

data_2020 = []
jumlah_harga = 0
euler = 2.71828
x=1
for i in data:
  data_2020.append([i[0],i[4]])

for i in data_2020:
  jumlah_harga += i[1]

x = 1
delta = jumlah_harga/34

probabilitas_2020 =  ( delta**(x) )   / x
print("probabilitas 2020 =","2.7182 **",delta,"*",probabilitas_2020)

data_2021 = []
jumlah_harga = 0
euler = 2.71828
x=1
for i in data:
  data_2021.append([i[0],i[5]])

for i in data_2021:
    jumlah_harga += i[1]

x = 1
delta = jumlah_harga/34

probabilitas_2021 =  ( delta**(x) )   / x
print("probabilitas 2021 =","2.7182 **",delta,"*",probabilitas_2021)


rata_2018_sampai_2019 = (probabilitas_2018+probabilitas_2019)/2
rata_2020_sampai_2021 = (probabilitas_2020+probabilitas_2021)/2
print("rata-rata probabilitas 2018-2019 =",rata_2018_sampai_2019)
print("rata-rata probabilitas 2020-2021 =",rata_2020_sampai_2021)