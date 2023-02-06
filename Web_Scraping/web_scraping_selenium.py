from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.emag.ro/')
# print(driver)

element = driver.find_element(by=By.ID, value="searchboxTrigger")
element.send_keys('iphone 14')
element.submit()

count_phones = driver.find_elements(by=By.CLASS_NAME, value="card-v2")
# print(len(count_phones))


for i in range(1, len(count_phones)+1):
    try:
        phone = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]')
    except Exception:
        phone = False
    if phone:
        if 'Gold' in phone.text and 'Apple iPhone 14 Pro Max' in phone.text:
            price = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]/div/div/div[4]/div[1]/p[2]').text
            transformed_price = price.strip().replace('.', '').replace(',', '.').split(' ')[0]
            if 7500 <= float(transformed_price) <= 8000:
                print(transformed_price)
                driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position="{i}"]/div/div/div[4]/div[2]/form/button').submit()

# for idx, i in enumerate(count_phones):
#     if 'Gold' in i.text and 'Apple iPhone 14 Pro Max' in i.text:
#         # print(i.text)
#         # print("\n----------------------------------------\n")
#         price = i.find_element(by=By.CLASS_NAME, value="product-new-price").text
#         # print(price)
#         transformed_price = price.strip().replace('.', '').replace(',', '.').split(' ')[0]
#         # print(transformed_price)
#         if 7500 <= float(transformed_price) <= 8000:
#             print(transformed_price)
#             driver.implicitly_wait(20)
#             # driver.find_element(by=By.XPATH, value='//*[@id="card_grid"]/div[8]/div/div/div[4]/div[2]/form/button').submit()
#             driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[@data-position={idx}]/div/div/div[4]/div[2]/form/button').submit()