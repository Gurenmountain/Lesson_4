from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

tim
my_account_menu = driver.find_element_by_link_text("My Account")
my_account_menu.click()

user_name_field = driver.find_element_by_id("username")
user_name_field.send_keys("test@email.com")

password_field = driver.find_element_by_id("password")
password_field.send_keys("Some HardPassword123!@#!@#")

login_btn = driver.find_element_by_name("login")
login_btn.click()

# Переход на вкладку Shop
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Открытие книги "Android Quick Start Guide"
android_quick_start_book = driver.find_element_by_css_selector(".post-169 h3")
android_quick_start_book.click()

# Получение значения новой и старой цены
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text

book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text

# Проверка значений цен
assert book_old_price_text == "₹600.00"
assert book_new_price_text == "₹450.00"

# Явное ожидание для обложки книги
book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))
)
book_cover.click()

# Явное ожидание для кнопки закрытия обложки книги в режиме предпросмотра
book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))
)
book_cover_close.click()
