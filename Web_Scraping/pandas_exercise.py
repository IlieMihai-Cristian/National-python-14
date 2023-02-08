import pandas as pd
# print(pd.__version__)
var = {'x': 1, 'y': 7, 'z': 2}
# var_series = pd.Series(var)
# print(var_series)
var_2 = [1, 7, 2]
var_series = pd.Series(var_2, index=['linie1', 'linie2', 'linie3'])  # ceea ce este trecuta in index redenumeste indecsii seriei (label)
# print(var_series)
# print(var_series[0], var_series['linie1'])

# print(pd.Series(var, index=['x', 'z']))

data = {
    "key1": [0, 1, 4],
    "key2": [3, 2, 5]
}

# var_3 =pd.DataFrame(data) # printeaza tabelul cu cheile din dat (denumire de coloana)
# print(var_3)

var_3 = pd.DataFrame(data, index=['linieA', 'linieB', 'linieC'])
# print(var_3)
# print(var_3['key1'])
# print(var_3.loc['linieA'])  # returneaza o Serie cu valorile liniei asociate indexului
# print(var_3.loc['linieA', 'key2'])  # returneaza o valoare dupa index(pozitie) si cheie(denumire coloana)
# print(var_3.loc['linieB':'linieC']) # returneaza o succesiune de randuri consecutive (serii) din Dataframe folosind slice
# print(var_3.loc[['linieA', 'linieC']]) # returneaza randuri multiple (serii) din Dataframe

# taskuri = {
#     'zile': [2, 4, 5],
#     'durata': [50, 40, 45]
# }
# var_df = pd.DataFrame(taskuri)
# print(var_df)

# taskuri['zile'][1] = 66
# print(taskuri)
# var_df['zile'].loc[1] = 66
# print(var_df)

# df = pd.read_excel('Curs_BNR_selenium.xlsx')
# # print(df)
# for x in df.index:
#     # print(x, df.loc[x, 'AED'])
#     if float(df.loc[x, 'AED']) > 1.2:
#         df.drop(x, inplace=True)
# # print(df)
# df.to_excel('Tabel_procesat.xlsx', index=0)

# df = pd.read_excel('Tabel_procesat.xlsx')
# print(df.corr())
# print(df.describe())
# df.describe().to_excel('Describe.xlsx')

var_a = pd.read_csv('test.csv')
# print(ionel)
# var_a.dropna(inplace=True)
# print(var_a)
# var_a.fillna(0, inplace=True)
# print(var_a)
# var_a['AL'].fillna(0, inplace=True)
# print(var_a)
# var_a.loc[6, 'CH'] = 93
# print(var_a)
# var_a.replace(': ', 0, inplace=True)
# var_a.replace(':', 0, inplace=True)
# print(var_a)

print(var_a.transpose())