import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://bnr.ro/files/xml/nbrfxrates2022.htm')
table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
# print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
# print(table_body.text)
header = table_head.text.split('\n')
body = table_body.text.split('\n')
# print(header)
# print(body)
# print(len(body))

# TABEL GENERAT PE RANDURI

# body_rows = []
# counter = 0
# for i in range(0, len(body), len(header)):
#     counter = i
#     body_rows.append(body[counter:counter+len(header)])
# print(body_rows)
#
# df = pd.DataFrame(body_rows, columns=header)
# print(df)
# df.to_excel("Curs_BNR_selenium.xlsx", index=False)

# TABEL GENERAT PE COLOANE

body_columns = {key: [] for key in range(len(header))}
# print(body_columns)

counter = 0
for j in body:
    body_columns[counter % len(header)].append(j)
    counter += 1

df = pd.DataFrame(body_columns)
print(df)
df.to_excel("Curs_BNR_selenium_2.xlsx", header=header, index=0)
