# 🧠 Brain MRI Anomaly Detection

Bu proje, **beyin tümörü tespiti** için MR görüntülerinde anomalilerin belirlenmesini hedefleyen bir yapay zeka sistemidir. Sistem, farklı algoritmalarla eğitilen modellerin karşılaştırılması ve en uygun modelin seçilmesi ile son kullanıcıya **grafiksel ve açıklamalı sonuçlar** sunan bir **Flask tabanlı web arayüzü** içermektedir.

This project is an artificial intelligence system that aims to identify anomalies in MRI images for brain tumor detection. The system includes a Flask-based web interface that compares models trained with different algorithms and selects the most appropriate model, presenting graphical and explanatory results to the end user.

## 🎯 Proje Amacı

Bu projenin amacı, beyin MR görüntüleri üzerinden anomali (tümör) tespiti yaparak doktorlara ve araştırmacılara destek olabilecek bir karar destek sistemi geliştirmektir. Aynı zamanda farklı algoritmaların performanslarını karşılaştırarak en verimli yapının belirlenmesi amaçlanmıştır.

The aim of this project is to develop a decision support system that can support doctors and researchers by detecting anomalies (tumors) on brain MRI images. It is also aimed to determine the most efficient structure by comparing the performances of different algorithms.

---

## 🧪 Kullanılan Algoritmalar

Veri seti 6 farklı algoritmayla eğitilmiş ve sonuçlar karşılaştırılmıştır:

- ✅ **Convolutional Neural Network (CNN)** + **ResNet50**
- ✅ **Autoencoder**
- ✅ **Variational Autoencoder (VAE)**
- ✅ **Isolation Forest**
- ✅ **One-Class SVM**
- ✅ **K-Means Clustering**

Tüm algoritmaların sonuçları **accuracy, precision, recall, F1-score ve ROC AUC** gibi metriklerle değerlendirilmiştir.

---

## 🧰 Kullanılan Teknolojiler

| Katman           | Teknoloji                          |
| ---------------- | ---------------------------------- |
| Backend          | Python, Flask                      |
| Machine Learning | TensorFlow, Keras, Scikit-learn    |
| Veri İşleme      | OpenCV, NumPy, Matplotlib, Seaborn |
| Arayüz           | HTML/CSS (Jinja2 ile), Bootstrap   |

---

## 🌐 Web Arayüz Özellikleri

- Görsel yükleme ve anında tahmin sonucu alma
- Tahmin sonuçlarının görsel grafiklerle sunulması
- Modelin sınıflandırma güven skoru
- Hastaya özel **öneri bölümü ("What to do next?")**
- PDF rapor çıktısı alma desteği
- Çoklu görsel yükleme desteği

---

## 🗂️ Proje Yapısı

```
brain_mri_anomaly_detection/
├── models/ # Eğitimli modeller (git ile yüklenmez)
├── utils/ # Yardımcı fonksiyonlar (veri ön işleme, tahmin vb.)
├── web/ # Flask tabanlı web uygulaması
├── run_cnn_model.py # CNN (ResNet50) modelini çalıştırma
├── run_autoencoder.py # Autoencoder çalıştırma
├── run_vae.py # VAE çalıştırma
├── run_isolation_forest.py
├── run_one_class_svm.py
├── run_kmeans.py
└── README.md
```

> Not: Büyük boyutlu `.keras` model dosyaları `.gitignore` içerisinde yer almaktadır.

---

## 🚀 Başlangıç

1. Gerekli kütüphaneleri yükleyin:

```
pip install -r requirements.txt
```

2. Flask uygulamasını başlatın:

```
cd web
python app.py
```

3. Tarayıcınızdan http://localhost:5000 adresine giderek uygulamayı kullanabilirsiniz.

## 👨‍💻 Geliştirici

**Arda Berk Koca**
[GitHub Profilim] -- (https://github.com/ArdaBerkKoca)

## 🧠 Kaynaklar

[Brain Tumor MRI Dataset - Kaggle] -- (https://www.kaggle.com/datasets/)

