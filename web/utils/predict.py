import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

CLASS_EN = ['glioma', 'meningioma', 'notumor', 'pituitary']
CLASS_TR = ['Glial Tümör', 'Meningiom', 'Tümör Yok', 'Hipofiz Tümörü']

MODEL_PATH = os.path.join("..", "models", "final_brain_tumor_model.keras")
model = load_model(MODEL_PATH)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)[0]
    predicted_index = np.argmax(preds)
    predicted_class = CLASS_EN[predicted_index]
    display_class = CLASS_TR[predicted_index]

    # Her görsel için ayrı grafik ismi oluştur
    filename = os.path.basename(img_path)
    chart_filename = f"{os.path.splitext(filename)[0]}_chart.png"
    chart_path = os.path.join("static", "results", chart_filename)

  # Grafik çiz
    plt.figure(figsize=(8, 5))
    bars = plt.bar(CLASS_TR, preds * 100, color='green')
    plt.title("Model Tahmin Sonucu")
    plt.ylabel("Olasılık (%)")
    plt.ylim(0, 100)
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2.0, bar.get_height(), f'{preds[i]*100:.1f}%', ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return predicted_class, display_class, preds, chart_path
