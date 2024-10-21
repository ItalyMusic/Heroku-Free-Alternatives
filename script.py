import os

# تثبيت المكتبات المطلوبة
os.system('pip install requests')
os.system('pip install beautifulsoup4')
os.system('pip install selenium')
os.system('pip install webdriver-manager')

# باقي الكود الخاص بك
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# إعداد WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# فتح الموقع
url = 'https://emojicombos.com/text-art'
driver.get(url)

# العثور على الزر والضغط عليه
button = driver.find_element(By.XPATH, "//button[contains(text(), '𝕞𝕒𝕜𝕖 𝓯𝓪𝓷𝓬𝔂 ᵗᵉˣᵗ')]")
button.click()

# انتظار تحميل النتائج
time.sleep(2)  # يمكنك تعديل الوقت حسب الحاجة

# جلب الرابط الجديد بعد الضغط على الزر
new_url = driver.current_url

# استخدام requests لجلب البيانات من الرابط الجديد
response = requests.get(new_url)
soup = BeautifulSoup(response.content, 'html.parser')

# استخراج البيانات المطلوبة
# على سبيل المثال، استخراج النصوص الجديدة
new_texts = soup.find_all('div', class_='new-text-class')  # عدل هذا حسب هيكل الصفحة
for text in new_texts:
    print(text.get_text())

# إغلاق المتصفح
driver.quit()
