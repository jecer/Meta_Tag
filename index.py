from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from time import sleep
import os
import sys


options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/102.0.5005.115 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
print('Результат будет в файле data.csv')
query = input('Введи запрос: ')
url = f'https://yandex.ru/search/?text={query}'


# number = int(input('Сколько страниц (не более 5):  '))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

browser = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options)
browser.implicitly_wait(1)
browser.get(url)
titles = []
descriptions = []
domens = []

try:
    eror = browser.find_element(By.CSS_SELECTOR, '#root > div > div > div.Spacer.'
                                                 'Spacer_auto-gap_bottom > div >'
                                                 ' form > div > div.CheckboxCaptcha-Anchor > input')
    eror.click()

    # search = browser.find_element(By.CSS_SELECTOR, '#uniq16547008090681')
    # search.clear()
    # search.send_keys(query)
    #
    # button = browser.find_element(By.CSS_SELECTOR, 'body > header > div > div > div.serp-header__search2 > form > '
    #                                                'div.search2__button > button')
    # button.click()

    all_ = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]')
    for x in range(3):
        for k in all_:
            h2 = browser.find_elements(By.XPATH, '//*[@id="search-result"]'
                                                 '//div/div[1]/a/h2/span')
            for i in h2:
                title = browser.find_element(By.XPATH, '//*[@id="search-result"]//div/div[3]/div/span')
                titles.append(i.text)
            description = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul//div/div[3]/div/span/label/span[2]')
            for d in description:
                description_ = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul//div/div[3]/div/span/label/span[2]')
                descriptions.append(d.text)
            link = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li/div/div[1]/a')
            for q in link:
                domen = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li/div/div[1]/a')
                domens.append(q.get_attribute('href'))
            page = browser.find_element(By.CSS_SELECTOR, 'body > div.main.serp.i-bem > div.main__center >'
                                                         ' div.main__content > div.content.i-bem > '
                                                         'div.content__left > div.pager.i-bem > div > '
                                                         'a.link.link_theme_none.link_target_serp.pager'
                                                         '__item.pager__item_kind_next.i-bem')
            sleep(1)
            page.click()

except:
    search = browser.find_element(By.CSS_SELECTOR, '#uniq16547008090681')
    search.clear()
    search.send_keys(query)

    button = browser.find_element(By.CSS_SELECTOR, 'body > header > div > div > div.serp-header__search2 > form > '
                                                   'div.search2__button > button')
    button.click()

    all_ = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]')
    for x in range(3):
        for k in all_:
            h2 = browser.find_elements(By.XPATH, '//*[@id="search-result"]//div/div[1]/a/h2/span')
            for i in h2:
                title = browser.find_element(By.XPATH, '//*[@id="search-result"]//div/div[3]/div/span')
                titles.append(i.text)
            description = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul//div/div[3]/div/span/label/span[2]')
            for d in description:
                description_ = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul//div/div[3]/div/span/label/span[2]')
                descriptions.append(d.text)
            link = browser.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li/div/div[1]/a')
            for q in link:
                domen = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li/div/div[1]/a')
                domens.append(q.get_attribute('href'))
            page = browser.find_element(By.CSS_SELECTOR, 'body > div.main.serp.i-bem > div.main__center >'
                                                         ' div.main__content > div.content.i-bem > '
                                                         'div.content__left > div.pager.i-bem > div > '
                                                         'a.link.link_theme_none.link_target_serp.pager'
                                                         '__item.pager__item_kind_next.i-bem')
            sleep(1)
            page.click()

if '...' in titles:
    del titles[titles.index('pest')]

with open(os.path.join(os.path.abspath("."), './data.csv'), 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(('Домен', 'Тайтл', 'Описание'))
    for i in zip(domens, titles, descriptions):
        writer.writerow(i)

sleep(1)
browser.close()
browser.quit()
