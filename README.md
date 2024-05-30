# Image Segmentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu proje, görüntü segmentasyonu yapmak için geliştirilmiş bir araçtır. Amacı, verilen görüntülerde belirli nesneleri veya bölgeleri otomatik olarak tanımlamak ve ayırmaktır.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Lisans](#lisans)


## Özellikler

- Görüntü segmentasyonu için çeşitli algoritmaların uygulanması
- Kolay kullanımlı arayüz
- Yüksek doğruluk oranı ile segmentasyon
- Çıktıların görselleştirilmesi ve kaydedilmesi

## Kurulum

Proje gereksinimlerini karşılamak için aşağıdaki adımları izleyin.

### Gereksinimler

- Python 3.8 veya üstü
- Git
- Virtualenv (tercihen)

### Adımlar

1. Repository'i klonlayın:
   ```sh
   git clone https://github.com/SultanDogan/imageSegmentation.git
   cd imageSegmentation
2. Sanal ortam oluşturun ve etkinleştirin:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows için: .\venv\Scripts\activate
3. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip install -r requirements.txt

Kullanım
Aşağıdaki komutları kullanarak projeyi çalıştırabilirsiniz.

Segmentasyon yapmak istediğiniz görüntüyü input klasörüne yerleştirin.
Segmentasyon algoritmasını çalıştırın:
  ```sh
  python ade20k_mmSeg.py --input input/your_image.jpg --output output/segmented_image.png
  ```
Sonuçlar output klasöründe kaydedilecektir.
Komut Satırı Seçenekleri
 -  --input: Segmentasyon yapılacak görüntü dosyasının yolu.
 -  --output: Segmentasyon sonucu kaydedilecek dosyanın yolu.


Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

