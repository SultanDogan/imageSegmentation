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
- Sınıf haritasının düzenlenmesi
- Kolay kullanımlı arayüz
- Yüksek doğruluk oranı ile segmentasyon
- Çıktıların görselleştirilmesi ve kaydedilmesi

## Kurulum

Proje gereksinimlerini karşılamak için aşağıdaki adımları izleyin.

### Gereksinimler

- Python 3.8 veya üstü
- Git
- Anaconda
- Virtualenv (tercihen)

### Adımlar

1. Repository'i klonlayın:
   ```sh
   git clone https://github.com/SultanDogan/imageSegmentation.git
   cd imageSegmentation
2. Sanal ortam oluşturun ve etkinleştirin:
   ```sh
   conda create --name mmsegmentation python=3.8 -y
   conda activate mmsegmentation
3. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip install -r requirements.txt
4. Gerekli config ve checkpoint dosyalarını yükleyin:
   ```sh
   mim download mmseg --config fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512 --dest ./checkpoints   #fastfcn
   mim download mmseg --config pspnet_r50-d8_4xb4-160k_ade20k-512x512 --dest ./checkpoints            #pspnet
   mim download mmseg --config upernet_r50_4xb4-80k_ade20k-512x512 --dest ./checkpoints               #upernet
   mim download mmseg --config deeplabv3_r50-d8_4xb4-80k_ade20k-512x512 --dest ./checkpoints          #deeplabv3
   
Not: (installationTutorial.ipynb - dosyasından da yardım alabilirsiniz.)

## Kullanım

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


## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

