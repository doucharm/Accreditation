
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json
from variables import data_source
def log_in_hanlder(driver,credentials):
    elem = driver.find_element(By.ID, "userNameInput")
    elem.clear()
    elem.send_keys(str(credentials['email']))
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element(By.ID, "passwordInput")
    elem.clear()
    elem.send_keys(str(credentials['password']))
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element(By.ID, "submitButton")
    elem.click()
def get_data_online(url,credentials) -> list:
    options = EdgeOptions()
    options.headless = True
    driver = Edge(options=options)
    driver.get(url)
    elem = driver.find_element(By.ID, "userNameInput")
    driver.refresh()
    #attempt to collect data from webpage
    data = driver.page_source
    driver.quit()
    return data
def get_data_local(file_name) -> list:
    data=None
    try:
        with open(file=file_name) as f:
            data=json.load(f)
    except Exception as e:
        print(e)
    return data
def data_format(data):
    formated_data=None
    try:
        #function to format data
        formated_data=data
    except Exception as e:
        print(e)
    finally:
        print('Successfully format data to workable format')
        return formated_data
def main():
    credentials={'email':'randomemail@unob.cz','password':'12345'}
    data = get_data_online(data_source,credentials=credentials)
    print(data)
if __name__ == '__main__':
    main()
