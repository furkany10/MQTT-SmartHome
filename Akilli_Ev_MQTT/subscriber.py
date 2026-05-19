import paho.mqtt.client as mqtt

# MQTT Broker Ayarları
BROKER_HOST = "localhost"
BROKER_PORT = 1883

# Bağlantı kurulduğunda çalışacak fonksiyon (Callback)
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Broker'a başarıyla bağlanıldı!")
        # 'ev/#' hiyerarşisindeki TÜM alt topic'lere abone oluyoruz
        topic_filtresi = "ev/#"
        client.subscribe(topic_filtresi)
        print(f"'{topic_filtresi}' altındaki tüm yayınlar dinleniyor...\n")
    else:
        print(f"Bağlantı başarısız, hata kodu: {rc}")

# Yeni bir mesaj (veri) geldiğinde çalışacak fonksiyon (Callback)
def on_message(client, userdata, msg):
    topic = msg.topic
    veri = msg.payload.decode("utf-8")
    
    # Gelen topic türüne göre ekrana düzgün çıktı yazdırma
    if "sicaklik" in topic:
        print(f"[YENİ MESAJ] Salon Sıcaklığı Alındı: {veri}°C (Topic: {topic})")
    elif "nem" in topic:
        print(f"[YENİ MESAJ] Mutfak Nemi Alındı: %{veri} (Topic: {topic})")
    else:
        print(f"[YENİ MESAJ] Konu: {topic} | Veri: {veri}")

# İstemci (Client) oluşturma
subscriber = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="Merkez_Kontrol_Subscriber")

# Fonksiyonları istemciye bağlama
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Bağlantıyı başlatma
subscriber.connect(BROKER_HOST, BROKER_PORT, 60)

# Sürekli dinleme döngüsü (Blocking loop)
try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("\nDinleme kullanıcı tarafından durduruldu.")
    subscriber.disconnect()