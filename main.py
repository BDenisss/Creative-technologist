import machine
import ssd1306
import network
import urequests
import time
import json
import utime

# Connexion Wi-Fi
ssid = 'iPhone14ProY'
password = '12345678'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        pass
    
    print('Connexion Wi-Fi réussie, adresse IP:', wlan.ifconfig()[0])

connect_wifi()

# Configuration de l'écran OLED
i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

cryptos = [
    {"name": "Bitcoin", "symbol": "BTC", "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"},
    {"name": "Ethereum", "symbol": "ETH", "url": "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"},
    {"name": "Litecoin", "symbol": "LTC", "url": "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd"},
    {"name": "Ripple", "symbol": "XRP", "url": "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"},
    {"name": "Cardano", "symbol": "ADA", "url": "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd"}
]

current_crypto = 0

def get_crypto_price(url):
    print("Récupération du prix...")
    response = urequests.get(url)
    print("Réponse brute de l'API:", response.text)  # Ajout du texte brut de la réponse pour débogage
    data = response.json()
    response.close()
    return data[list(data.keys())[0]]['usd']  # Accéder au prix en USD

def button_callback(pin):
    global current_crypto
    current_crypto = (current_crypto + 1) % len(cryptos)
    print("Cryptomonnaie actuelle:", cryptos[current_crypto]['name'])

# Configuration du bouton
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

def display_info(name, price):
    oled.fill(0)
    oled.text("{} Price:".format(name), 0, 0)
    oled.text("$ {:.2f}".format(price), 0, 10)
    current_time = utime.localtime()
    oled.text("Last Update:", 0, 20)
    oled.text("{:02d}/{:02d}/{:02d}".format(current_time[2], current_time[1], current_time[0]), 0, 30)
    oled.text("{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5]), 0, 40)
    oled.show()

while True:
    try:
        crypto = cryptos[current_crypto]
        price = get_crypto_price(crypto['url'])
        display_info(crypto['name'], price)
        time.sleep(5)  # Mise à jour toutes les 5 secondes pour voir les changements plus rapidement
    except Exception as e:
        print("Erreur lors de la récupération des données:", e)
