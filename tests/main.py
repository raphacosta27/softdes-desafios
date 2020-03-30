import argparse
from selenium import webdriver
import os
import time

username = 'admin'
passwd = 'admin'
path_to_desafio1 = "/Users/raphacosta/Desktop/Insper9/softdes-desafios/tests/desafio1.py"
path_to_desafio2 = "/Users/raphacosta/Desktop/Insper9/softdes-desafios/tests/desafio2.py"


parser = argparse.ArgumentParser(description='Choose browser driver')
parser.add_argument('--browser', metavar='b', type=str,
                    help='Type your browser as browser=chrome or browser=firefox')



args = parser.parse_args()
if args.browser == 'chrome':
    browser = webdriver.Chrome(executable_path='drivers/chromedriver')
elif args.browser == 'firefox':
    browser = webdriver.Firefox(executable_path='drivers/geckodriver')
else:
    raise('Select a valid browser')



browser.get(f'http://{username}:{passwd}@localhost:8000/')
element = browser.find_element_by_xpath('//*[@id="resposta"]')
element = element.send_keys(path_to_desafio1)
browser.implicitly_wait(20)
enviar = browser.find_element_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/form/button')
enviar.click()
# ver se deu bom

# browser.implicitly_wait(2)
# time.sleep(4)

browser.get(f'http://{username}:{passwd}@localhost:8000/')
element = browser.find_element_by_xpath('//*[@id="resposta"]')
element = element.send_keys(path_to_desafio2)
browser.implicitly_wait(20)
enviar = browser.find_element_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/form/button')
enviar.click()
# ver se deu bom

browser.close()
### pytest
