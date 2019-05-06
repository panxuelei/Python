from selenium import webdriver
import time

# Creating an instance webdriver
browser = webdriver.Chrome('chromedriver.exe')

# 打开google
# browser.fullscreen_window()
browser.get('https://www.google.com')

# # Sign in by id
# browser.find_element_by_id('gb_70').click()

# # 查询 by name
# browser.find_element_by_name('q').send_keys('郭文贵\n')

# # Gmail by link text
# browser.find_element_by_link_text('Gmail').click()
# time.sleep(3)
# browser.back()
# time.sleep(2)
# browser.find_element_by_partial_link_text('mail').click()
# time.sleep(3)

# # by tag
# elements = browser.find_elements_by_tag_name('a')
# # print(elements)
# # print(len(elements))
# for element in elements:
#     # print(element.text)
#     if 'Gmail' in element.text:
#         # time.sleep(2)
#         element.click()
#
# time.sleep(2)

# # by class name
# time.sleep(2)
# for element in browser.find_elements_by_class_name('Fx4vi'):
#     print(element.text)
#     if element.text == 'Google 大全':
#         element.click()

# by xPath
time.sleep(2)
browser.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()
time.sleep(5)
browser.quit()