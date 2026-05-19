# MQTT-SmartHome
# BIL214 Bilgisayar Ağları - MQTT Tabanlı Akıllı Ev Sistemi 🏠

Bu proje, BIL214 Bilgisayar Ağları dersi kapsamında MQTT (Message Queuing Telemetry Transport) protokolü kullanılarak geliştirilmiş bir Publish-Subscribe mesajlaşma sistemidir. Sistem, tek bir bilgisayar (localhost) üzerinde **Mosquitto Broker** aracılığıyla haberleşen bir **Publisher** (veri gönderen) ve bir **Subscriber** (veri alan) uygulamasından oluşmaktadır.

## 📌 Senaryo: Akıllı Ev Sistemi
Projede "Akıllı Ev" senaryosu temel alınmıştır. 
* **Publisher:** Evin farklı odalarındaki (salon ve mutfak) sensörleri simüle eder. Rastgele sıcaklık ve nem verileri üreterek hiyerarşik konu başlıklarına (topic) yayınlar.
* **Subscriber:** `ev/#` joker (wildcard) karakterini kullanarak ev ile ilgili tüm sensör verilerine abone olur ve gelen mesajları anlık olarak terminal ekranına yazdırır.

**Kullanılan Topic Yapıları:**
* `ev/salon/sicaklik`
* `ev/mutfak/nem`

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python 3.x
* **MQTT İstemci Kütüphanesi:** paho-mqtt
* **MQTT Broker:** Eclipse Mosquitto
* **Ağ Analizi:** Wireshark

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayınız:

### 1. Gereksinimlerin Kurulması
Bilgisayarınızda Python kurulu olduğundan emin olun. Ardından terminal üzerinden MQTT kütüphanesini indirin:
```bash
pip install paho-mqtt

2. Mosquitto Broker'ın Başlatılması
Eclipse Mosquitto'yu kurduktan sonra varsayılan ayarlarla (1883 portu) arka planda çalıştığından emin olun veya terminalden manuel olarak başlatın:

Bash
mosquitto -v
3. İstemcilerin Çalıştırılması
İki farklı terminal penceresi açın. İlk pencerede dinleyici (subscriber) uygulamasını başlatın:

Bash
python subscriber.py
Dinleyici bekleme moduna geçtikten sonra, ikinci terminal penceresinde veri gönderici (publisher) uygulamasını başlatın:

Bash
python publisher.py

Verilerin anlık olarak üretildiği ve subscriber terminaline düştüğü görülecektir. İşlemleri durdurmak için terminallerde CTRL+C komutunu kullanabilirsiniz.

📊 Wireshark Ağ Analizi
Proje dosyaları içerisinde bulunan .pcapng uzantılı dosya, sistemin yerel ağ (loopback) üzerindeki MQTT trafiğinin Wireshark ile alınmış kayıtlarını içerir. Bu kayıtlar üzerinden cihazların broker'a bağlanma (Connect), abone olma (Subscribe) ve şifresiz veri iletimi (Publish) paketleri incelenebilir.
