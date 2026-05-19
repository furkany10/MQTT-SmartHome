import time
import random
import paho.mqtt.client as mqtt

# MQTT Broker Ayarları
BROKER_HOST = "localhost"  # Aynı bilgisayarda çalıştığı için local
BROKER_PORT = 1883         # Varsayılan MQTT portu

# İstemci (Client) oluşturma
publisher = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="Ev_Sensor_Publisher")

print("MQTT Broker'a bağlanılıyor...")
publisher.connect(BROKER_HOST, BROKER_PORT, 60)

print("Akıllı Ev Veri Yayını Başladı... (Durdurmak için CTRL+C)")

try:
    while True:
        # 1. Rastgele Sıcaklık Verisi Üret ve Gönder
        sicaklik = round(random.uniform(20.0, 26.0), 1)
        topic_sicaklik = "ev/salon/sicaklik"
        publisher.publish(topic_sicaklik, str(sicaklik), qos=1)
        print(f"[YAYINLANDI] -> Topic: {topic_sicaklik} | Değer: {sicaklik}°C")
        
        # 2. Rastgele Nem Verisi Üret ve Gönder
        nem = round(random.uniform(40.0, 60.0), 1)
        topic_nem = "ev/mutfak/nem"
        publisher.publish(topic_nem, str(nem), qos=1)
        print(f"[YAYINLANDI] -> Topic: {topic_nem} | Değer: %{nem}")
        
        print("-" * 40)
        time.sleep(3) # 3 saniyede bir veri gönderir

except KeyboardInterrupt:
    print("\nYayın kullanıcı tarafından durduruldu.")
    publisher.disconnect()