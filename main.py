from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from variables import data_source
import time
def log_in_hanlder(driver,credentials):
    username_field = driver.find_element(By.NAME, "Username")
    username_field.clear()
    username_field.send_keys(credentials['email'])
    time.sleep(0.5)
    
    password_field = driver.find_element(By.NAME, "Password") 
    password_field.clear()
    password_field.send_keys(credentials['password'])
    time.sleep(0.5)
    
    password_field.send_keys(Keys.RETURN)
    time.sleep(0.5)
    print("Finish logging in")
def get_data_online(url,credentials) -> list:
    options = EdgeOptions()
    options.headless = True
    driver = Edge(options=options)
    driver.get(url)
    driver.refresh()
    try:
        log_in_hanlder(driver=driver,credentials=credentials)
    except:
        print(Exception)
    #attempt to collect data from webpage
    matches = driver.find_element(By.TAG_NAME, "pre").text
    data = json.loads(matches)
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
def store_data(data):
   with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
def main():
    from credentials import get_credentials
    credentials=get_credentials()
    data = get_data_online(data_source,credentials=credentials)
    store_data(data=data)
if __name__ == '__main__':
    main()
