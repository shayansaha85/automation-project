from selenium import webdriver
import time as t

def save_logo(driver, xpath_of_image, name, folder):
    t.sleep(5)
    with open(f'{folder}/{name}', 'wb') as file:
        file.write(driver.find_element_by_xpath(xpath_of_image).screenshot_as_png)
    print(f"{name} saved in {folder}")