from selenium import webdriver

# Creating an instance webdriver
browser = webdriver.Chrome('E:\Others\installer\exe\chromedriver.exe')
# browser.fullscreen_window()
browser.get('https://www.google.com')
browser.find_element_by_id('gb_70').click()
