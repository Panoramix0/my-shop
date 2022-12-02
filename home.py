import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# добавление комментария
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.execute_script("window.scrollBy(0, 600);")  # скролл страницы на 600 пикселей
# time.sleep(5)
Book_Selenium_Ruby = driver.find_element_by_css_selector(".post-160 > a.woocommerce-LoopProduct-link > h3").click()
Btn_Reviews = driver.find_element_by_class_name("reviews_tab").click()
time.sleep(3)
Your_Rating_5 = driver.find_element_by_class_name("star-5").click()
Review = driver.find_element_by_id("comment")
Review.send_keys("Nice book!")
Name = driver.find_element_by_id("author")
Name.send_keys("Aleksey")
Email = driver.find_element_by_id("email")
Email.send_keys("alexeyvas_96@mail.ru")
Btn_submit = driver.find_element_by_name("submit").click()
driver.quit()