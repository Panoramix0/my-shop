# import time
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# # регистрация аккаунта
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# My_Account = driver.find_element_by_id("menu-item-50").click()
# Email_Register = driver.find_element_by_id("reg_email")
# Email_Register.send_keys("alexeyvas_96@mail.ru")
# Password_Register = driver.find_element_by_id("reg_password")
# Password_Register.send_keys("P_a_s_s_WORD_96*_*")
# time.sleep(8)
# Btn_Register = driver.find_element_by_name("register").click()
# driver.quit()

import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# логин в систему
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
My_Account = driver.find_element_by_id("menu-item-50").click()
Email_Login = driver.find_element_by_id("username")
Email_Login.send_keys("alexeyvas_96@mail.ru")
Password_Login = driver.find_element_by_id("password")
Password_Login.send_keys("P_a_s_s_WORD_96*_*")
time.sleep(3)
Btn_Login = driver.find_element_by_name("login").click()
# Проверка, что элемент Logout есть на странице
tab_Logout = driver.find_element_by_link_text("Logout")
element_check = tab_Logout.get_attribute("value")
print("element_check:", tab_Logout.text)
assert tab_Logout.text == "Logout"
driver.quit()