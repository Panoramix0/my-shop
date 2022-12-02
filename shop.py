# import time
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# # отображение страницы товара
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# My_Account = driver.find_element_by_id("menu-item-50").click()
# Email_Login = driver.find_element_by_id("username")
# Email_Login.send_keys("alexeyvas_96@mail.ru")
# Password_Login = driver.find_element_by_id("password")
# Password_Login.send_keys("P_a_s_s_WORD_96*_*")
# time.sleep(3)
# Btn_Login = driver.find_element_by_name("login").click()
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# Book_HTML_5_Forms = driver.find_element_by_css_selector("li.post-181 > a.woocommerce-LoopProduct-link").click()
# # Проверяем, что заголовок книги называется HTML5 Forms
# Book_title = driver.find_element_by_class_name("product_title.entry-title")
# element_check = Book_title.get_attribute("value")
# print("element_check:", Book_title.text)
# assert Book_title.text == "HTML5 Forms"
# driver.quit()


# import time
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# # количество товаров в категории
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# My_Account = driver.find_element_by_id("menu-item-50").click()
# Email_Login = driver.find_element_by_id("username")
# Email_Login.send_keys("alexeyvas_96@mail.ru")
# Password_Login = driver.find_element_by_id("password")
# Password_Login.send_keys("P_a_s_s_WORD_96*_*")
# time.sleep(3)
# Btn_Login = driver.find_element_by_name("login").click()
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# time.sleep(3)
# Category_HTML = driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()
# # Book_count = driver.find_elements_by_css_selector(".cat-item.cat-item-19.current-cat > span")
# Book_count = driver.find_elements_by_css_selector("#content > ul > li.product")
# if len(Book_count) == 3:
#     print("На странице 3 товара(книги)") # len здесь посчитает количество элементов, найденных при помощи find_elements
# else:
#     print("Ошибка. Количество товаров(книг) на странице: " + str(len(Book_count)))
# driver.quit()



# import time
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# сортировка товаров
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# My_Account = driver.find_element_by_id("menu-item-50").click()
# Email_Login = driver.find_element_by_id("username")
# Email_Login.send_keys("alexeyvas_96@mail.ru")
# Password_Login = driver.find_element_by_id("password")
# Password_Login.send_keys("P_a_s_s_WORD_96*_*")
# time.sleep(3)
# Btn_Login = driver.find_element_by_name("login").click()
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# time.sleep(3)
# Selector = driver.find_element_by_name("orderby")
# select = Select(Selector)
# select.select_by_value("menu_order")
# time.sleep(3)
# print("selector_value:", select.first_selected_option.get_attribute("value"))
# if select.first_selected_option.get_attribute("value") == "menu_order":
#     print("Выбрано значение Default sorting")
# else:
#     print("Выбрано другое значение из списка")
# Selector = driver.find_element_by_name("orderby")
# select = Select(Selector)
# select.select_by_value("price-desc")
#
# Selector = driver.find_element_by_name("orderby")
# select = Select(Selector)
# select.select_by_value("price-desc")
# print("selector_value:", select.first_selected_option.get_attribute("value"))
# if select.first_selected_option.get_attribute("value") == "price-desc":
#     print("Выбрано значение сортировки  по цене от большей к меньшей (Sort by price: high to low)")
# else:
#     print("Выбрано другое значение сортировки из списка")


# отображение, скидка товара
# import time
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# My_Account = driver.find_element_by_id("menu-item-50").click()
# Email_Login = driver.find_element_by_id("username")
# Email_Login.send_keys("alexeyvas_96@mail.ru")
# Password_Login = driver.find_element_by_id("password")
# Password_Login.send_keys("P_a_s_s_WORD_96*_*")
# time.sleep(3)
# Btn_Login = driver.find_element_by_name("login").click()
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# Book_Android_QSG = driver.find_element_by_css_selector(".post-169 > a.woocommerce-LoopProduct-link > img").click()
# Book_old_price = driver.find_element_by_css_selector("del > .woocommerce-Price-amount.amount")
# Book_old_price_text = Book_old_price.text
# assert Book_old_price_text == "₹600.00"
# Book_new_price = driver.find_element_by_css_selector("ins > span")
# Book_new_price_text = Book_new_price.text
# assert Book_new_price_text == "₹450.00"
# Book_cover = WebDriverWait(driver, 8).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images ")) )
# Book_cover.click()
# Book_cover_close = WebDriverWait(driver, 8).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close ")) )
# Book_cover_close.click()
# driver.quit()


# # проверка цены в корзине
# import time
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# ADD_TO_BASKET_btn = driver.find_element_by_css_selector(".post-182 > a.button").click() # добавляем книгу "HTML5 WebApp Develpment" в корзину
# time.sleep(5)
# # Проверяем, что в корзине 1 товар
# Items_cart = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
# Items_cart_text = Items_cart.text
# print(Items_cart_text)
# assert Items_cart_text == "1 Item"
# # Проверяем что книга стоит "₹180.00"
# price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
# price_text = price.text
# print(price_text)
# assert price_text == "₹180.00"
# # Переходим в корзину
# Items_cart.click()
# # проверяем, что в Subtotal отобразилась стоимость
# Subtotal = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, " tr.cart-subtotal > td"), "₹180.00"))
# # проверяем, что в Total отобразилась стоимость
# Total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "  tr.order-total > td"), "₹183.60"))
# driver.quit()



# # работа в корзине
# import time
# from selenium import webdriver # импортируем webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# Tab_Shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")  # скролл страницы на 300 пикселей
# # добавляем книгу "HTML5 WebApp Develpment" в корзину
# ADD_TO_BASKET_btn = driver.find_element_by_css_selector(".post-182 > a.button").click()
# time.sleep(3)
# # добавляем книгу "JS Data Structures and Algorithm" в корзину
# ADD_TO_BASKET_btn2 = driver.find_element_by_css_selector(".post-180 > a.button").click()
# time.sleep(3)
# #  Переходим в корзину
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# time.sleep(3)
# # удаление первой книги "HTML5 WebApp Develpment"
# Deleting_book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a").click()
# time.sleep(3)
# # Нажатие на  Undo (отмена удаления)
# Undo = driver.find_element_by_css_selector("div.woocommerce-message > a").click()
# # увеличиваем количесто товара до 3 шт для "JS Data Structures and Algorithm“
# Three_books = driver.find_element_by_css_selector("[type='number']").clear()
# Three_books1 = driver.find_element_by_css_selector("[type='number']")
# Three_books1.send_keys("3")
# # Нажимаем на кнопку Update_Basket
# Update_Basket_btn = driver.find_element_by_name("update_cart").click()
# # Проверяем, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# Three_books1_check = Three_books1.get_attribute('value')
# print(Three_books1_check)
# assert Three_books1_check == "3"
# time.sleep(3)
# # Нажимаем на кнопку "APPLY COUPON"
# APPLY_COUPON_btn = driver.find_element_by_name("apply_coupon").click()
# time.sleep(3)
# # Проверяем, что появилось сообщение: "Please enter a coupon code." после нажатия на кнопку "APPLY COUPON"
# Checking_a_message = driver.find_element_by_css_selector("ul.woocommerce-error > li")
# Checking_a_message_ch = Checking_a_message.get_attribute("value")
# print("Checking_a_message_ch:", Checking_a_message.text)
# assert Checking_a_message.text == "Please enter a coupon code."
# driver.quit()



# покупка товара
import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
driver.get("http://practice.automationtesting.in/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
Tab_Shop = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")  # скролл страницы на 300 пикселей
# добавляем книгу "HTML5 WebApp Develpment" в корзину
ADD_TO_BASKET_btn = driver.find_element_by_css_selector(".post-182 > a.button").click()
time.sleep(3)
# Переходим в корзину
cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
time.sleep(3)
# Добавляем явное ожидание для кнопки "PROCEED TO CHECKOUT"
Expectation_btn = WebDriverWait(driver, 10).until( # говорим Selenium проверять в течение 10 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
# Нажимаем на кнопку "PROCEED TO CHECKOUT"
PROCEED_TO_CHECKOUT_btn = driver.find_element_by_class_name("checkout-button").click()
# Добавляем явное ожидание для поле first name, (ПОДУМАТЬ над ожиданием)
first_name = WebDriverWait(driver, 10).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.ID, "billing_first_name")) )
# Заполение обязательных полей
# first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Aleksey")
Last_Name = driver.find_element_by_id("billing_last_name")
Last_Name.send_keys("Vasiliev")
Email = driver.find_element_by_name("billing_email")
Email.send_keys("alexeyvas_96@mail.ru")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("89811063257")
time.sleep(3)
Selector = driver.find_element_by_id("s2id_billing_country").click()
time.sleep(3)
Search_line = driver.find_element_by_id("s2id_autogen1_search")
Search_line.send_keys("Russia")
time.sleep(3)
# Country_Rus = driver.find_element_by_id("select2-result-label-3564")
Country_Rus = driver.find_element_by_css_selector(".select2-results-dept-0.select2-result.select2-result-selectable").click()
Street_Address = driver.find_element_by_name("billing_address_1")
Street_Address.send_keys("Ivanovskaya")
City = driver.find_element_by_name("billing_city")
City.send_keys("St. Petersburg")
County = driver.find_element_by_name("billing_state")
County.send_keys("Russia")
Postcode_ZIP = driver.find_element_by_name("billing_postcode")
Postcode_ZIP.send_keys("197229")
driver.execute_script("window.scrollBy(0, 600);")  # скролл страницы на 600 пикселей
time.sleep(5)
# Выбираем метод оплаты: "Check Payments"
Check_Payments = driver.find_element_by_id("payment_method_cheque").click()
# Нажимаем на кнопку PLACE ORDER
PLACE_ORDER_btn = driver.find_element_by_name("woocommerce_checkout_place_order").click()
# Проверяем, что отображается надпись "Thank you. Your order has been received.", используя явное ожидание
Checking_the_inscription = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# Проверяем, что в методе оплаты (Payment Method) отображается текст "Check Payments"
Payment_Method = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
# driver.quit()


