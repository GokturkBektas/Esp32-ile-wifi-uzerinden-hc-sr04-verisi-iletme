import network
import socket
import time
from hcsr04 import HCSR04
from machine import Pin

triq = Pin(15,Pin.OUT)
eqho = Pin(2,Pin.IN)

a = HCSR04(triq,eqho)


# Wi-Fi ağ bilgilerini girin
WIFI_SSID = "Galaxy"
WIFI_PASSWORD = "12365432"

# Bağlanılacak sunucunun IP adresi ve port numarası
SERVER_IP = "192.168.91.114"  # Bilgisayarınızın IP adresi
SERVER_PORT = 80

# Wi-Fi istemcisini başlat
wifi_client = network.WLAN(network.STA_IF)
wifi_client.active(True)

# Wi-Fi ağına bağlan
wifi_client.connect(WIFI_SSID, WIFI_PASSWORD)

# Bağlantı sağlanana kadar bekleyin
while not wifi_client.isconnected():
    pass

# IP adresini alın
ip_address = wifi_client.ifconfig()[0]
print("Wi-Fi bağlantısı başarıyla sağlandı.")
print("IP Adresi:", ip_address)

# TCP istemcisini başlat
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))  # Sunucuya bağlan

# Veri gönderme döngüsü
while True:
    b= a.distance_cm()
    message = str(b)
    client_socket.send(message.encode())  # Veriyi sunucuya gönder
    print("Gönderilen veri:", message)
    time.sleep(0.25)  # Bir saniye bekleyin
