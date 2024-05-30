import mmcv
from mmseg.apis import inference_model, init_model
from mmseg.datasets import ADE20KDataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cv2

# Önceden eğitilmiş modelini seç
def select_model(model_name):
    model_names = {1: 'fastfcn', 2: 'pspnet', 3: 'upernet', 4: 'deeplabv3'}
    if model_name == 1:
        config_file = 'checkpoints/fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512.py'
        checkpoint_file = 'checkpoints/fastfcn_r50-d32_jpu_enc_512x512_80k_ade20k_20210930_225214-65aef6dd.pth'
    elif model_name == 2:
        config_file = 'checkpoints/pspnet_r50-d8_4xb4-160k_ade20k-512x512.py'
        checkpoint_file = 'checkpoints/pspnet_r50-d8_512x512_160k_ade20k_20200615_184358-1890b0bd.pth'
    elif model_name == 3:
        config_file = 'checkpoints/upernet_r50_4xb4-80k_ade20k-512x512.py'
        checkpoint_file = 'checkpoints/upernet_r50_512x512_80k_ade20k_20200614_144127-ecc8377b.pth'
    elif model_name == 4:
        config_file = 'checkpoints/deeplabv3_r50-d8_4xb4-80k_ade20k-512x512.py'
        checkpoint_file = 'checkpoints/deeplabv3_r50-d8_512x512_80k_ade20k_20200614_185028-0bb3f844.pth'
    else:
        raise ValueError("Geçersiz model adı")
    return config_file, checkpoint_file

# Model seçimi
model_name = 1  #(1:'fastfcn', 2:'pspnet', 3:'upernet',4:'deeplabv3')
config_file, checkpoint_file = select_model(model_name)
# Modeli başlat
model = init_model(config_file, checkpoint_file, device='cuda:0')

# ADE20K sınıf haritası ve yeni palet tanımı
class_mapping_ade20k = {
    0: None,  # arkaplanı yok say
    1: [4, 9, 17],  # 'vegetation' : tree, grass, plant
    2: [1, 25],  # 'buildings': building, house
    3: [2],  # 'sky': sky
    4: [6],  # 'roads': road
    5: [12],  # 'person' : person
    6: [20, 80, 83, 90, 91, 102, 103],  # 'vehicle' : car, bus,truck , airplane, van, ship
    7: [11],  # 'sidewalk' : sidewalk
    8: [255],  # ignore label
}

# ADE20K veri setindeki orijinal sınıf isimleri
class_names = ADE20KDataset.METAINFO['classes']
original_palette = ADE20KDataset.METAINFO['palette']

# Yeni paleti oluştur
new_palette = np.zeros((len(class_mapping_ade20k), 3), dtype=np.uint8)
for new_class, old_classes in class_mapping_ade20k.items():
    if old_classes is None:
        continue
    if isinstance(old_classes, int):
        old_classes = [old_classes]
    for old_class in old_classes:
        if old_class < len(original_palette):
            new_palette[new_class] = original_palette[old_class]

new_classes = ['background', 'vegetation', 'buildings', 'sky', 'roads', 'person', 'vehicle', 'sidewalk', 'ignore']

# Görselleştirme fonksiyonu
def visualize_segmentation_and_save(image_path, model, class_mapping, new_palette, new_classes, result_path, alpha=0.5):
    img = mmcv.imread(image_path)

    # Görüntüyü model ile segmentasyon yap
    result = inference_model(model, img)

    # Segmentasyon sonucunu alın
    seg_map = result.pred_sem_seg.data.squeeze().cpu().numpy()

    # Yeniden sınıflandırma ve renklendirme
    color_seg = np.zeros((seg_map.shape[0], seg_map.shape[1], 3), dtype=np.uint8)
    for new_class, old_classes in class_mapping.items():
        if old_classes is None:
            continue
        if isinstance(old_classes, int):
            old_classes = [old_classes]
        for old_class in old_classes:
            color_seg[seg_map == old_class] = new_palette[new_class]

    # Görselleştirme
    plt.figure(figsize=(img.shape[1] / 100, img.shape[0] / 100))  # Görüntü boyutuna göre şekil boyutunu ayarla
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.imshow(color_seg, alpha=alpha)

    # Sınıf etiketlerini ekle
    patches = []
    for new_class, class_name in enumerate(new_classes):
        if class_name != 'ignore' and class_name != 'background':
            patches.append(mpatches.Patch(color=new_palette[new_class] / 255.0, label=class_name))

    # Legendi ekle
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize='large')

    plt.axis('off')
    plt.savefig(result_path, bbox_inches='tight', pad_inches=0, dpi=100)  # Görseli kaydet
    plt.show()

# Örnek bir görsel ve segmentasyon haritası yolunu girin
image_path = '001.png'  # kendi görüntü yolunuzu girin
result_path = 'result_ade20k.jpg'
visualize_segmentation_and_save(image_path, model, class_mapping_ade20k, new_palette, new_classes, result_path, alpha=0.5)
