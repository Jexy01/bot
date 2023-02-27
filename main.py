import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup 
import csv

bot = telebot.TeleBot("6092711284:AAG9otheitc7duEaLYn8Bkb3geLaCIAl4Gc")

@bot.message_handler(commands=["start"])

def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1 = types.KeyboardButton(text="Apple")
    keyboard2 = types.KeyboardButton(text="Lenovo")
    keyboard3 = types.KeyboardButton(text="HP")
    keyboard4 = types.KeyboardButton(text="Acer")
    keyboard5 = types.KeyboardButton(text="Huawei")
    keyboard6 = types.KeyboardButton(text="Asus")
    # keyboard8 = types.KeyboardButton(text="/start")
    markup.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6)
    bot.send_message(chat_id, f"Привет {first_name} !\n" 
                    "Выберите название:", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Apple':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/218"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

        if message.text == 'Acer':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/313?brand%5B%5D=21&price_min=0&price_max=35190000"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

        if message.text == 'Lenovo':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/313?brand%5B%5D=19&price_min=0&price_max=24750000"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

        if message.text == 'Asus':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/313?brand%5B%5D=22&price_min=2268000&price_max=15768000"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

        if message.text == 'HP':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/313?brand%5B%5D=24&price_min=0&price_max=35190000"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

        if message.text == 'Huawei':
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/313?brand%5B%5D=55&price_min=80&price_max=91510000"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block swiper-slide")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    try:
                        product_link = link + item.find("a", class_="product_list_img slide").get("href")
                    except AttributeError:
                        product_price='нет в наличии!'
                    all_products = f"{product_name}\nЦена : {product_price}\nСсылка : {product_link}"
                    bot.send_message(chat_id, all_products)
                    write_csv({
                        'name':product_name,
                        'price':product_price,
                        'link':product_link
                    })

def write_csv(data):
    with open('laptops.csv', 'a') as file:
        names = ['name', 'price','link']
        write = csv.DictWriter(file, delimiter=' ', fieldnames=names)
        write.writerow(data)

bot.polling()
