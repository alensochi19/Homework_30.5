import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Alex/PycharmProjects/driver/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_check_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('alen.sochi19@gmail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('Alen191919!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

def test_all_pets_are_present():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('alen.sochi19@gmail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Alen191919!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 3).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
   # Сохранение данных о количестве питомцев из статистики
   user_information = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   user_information = user_information[0].text.split()
   total_pets = int(user_information[2])

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 3).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   number_pets = len(pets)
   # print(f'Количество по статистике: {total_pets}/n Присутствует на сайте: {number_pets} ')

   assert total_pets == number_pets

def test_half_have_photo():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('alen.sochi19@gmail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Alen191919!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
   user_information = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   user_information = user_information[0].text.split()
   total_pets = int(user_information[2])
   half = total_pets // 2

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 3).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover img')))
   pet_photo = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
   photo = 0
   for i in range(len(pet_photo)):
       if pet_photo[i].get_attribute('src') != '':
        photo += 1
   assert photo >= half

   user_information = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
   user_information = user_information[0].text.split()
   total_pets = int(user_information[2])
   half = total_pets // 2

def test_all_attribute():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('alen.sochi19@gmail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Alen191919!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

   # Установка неявного ожидания
   pytest.driver.implicitly_wait(3)
   images = pytest.driver.find_elements(By.XPATH, '//img[@id="all_my_pets"]')
   # Установка неявного ожидания
   pytest.driver.implicitly_wait(3)
   names = pytest.driver.find_elements(By.XPATH, '//td[1][@id="all_my_pets"]')
   # Установка неявного ожидания
   pytest.driver.implicitly_wait(3)
   descriptions = pytest.driver.find_elements(By.XPATH, '//td[2][@id="all_my_pets"]')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

def test_name():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('alen.sochi19@gmail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Alen191919!')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 3).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
   all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
   pet_names = []
   for i in all_pets:
      pet_names.append(i.text.split(' ')[0])
      print(pet_names)

   pet_names_1 = set(pet_names)
   if len(pet_names) == len(pet_names_1):
      print("Все имена уникальны")
   else:
      print("Есть одинаковые имена")

