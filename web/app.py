from flask import Flask, render_template, request
import numpy as np
from werkzeug.utils import secure_filename
import os
from utils.predict import predict_image
from utils.pdf_generator import generate_pdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("files")
        predictions = []

        for file in files:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            pred_class, display_class, probabilities, chart_path = predict_image(filepath)
            confidence = f"{np.max(probabilities) * 100:.1f}%"
            advice = generate_advice(pred_class)

            predictions.append({
                "filename": filename,
                "image_path": filepath,
                "display_class": display_class,
                "confidence": confidence,
                "advice": advice,
                "chart_path": chart_path
            })

        pdf_path = generate_pdf(predictions)
        return render_template("index.html", predictions=predictions, pdf_path=pdf_path)

    return render_template("index.html")

def generate_advice(pred_class):
    pred_class = pred_class.lower()
    if pred_class == "glioma":
        return "Tespit edilen tümör türü: GLIOMA. Glial hücrelerden köken alan bu tümörler beyin içinde derin dokulara yayılabilir. Düşük dereceli gliomlar yavaş büyürken, yüksek dereceliler agresif seyredebilir. Erken tanı tedavi başarısını artırır. Lütfen beyin cerrahisi veya onkoloji uzmanına danışınız."
    elif pred_class == "meningioma":
        return "Tespit edilen tümör türü: MENINGIOMA. Beyin zarından (meninks) kaynaklanan genellikle iyi huylu bir tümördür. Ancak büyüdükçe komşu dokulara baskı yapabilir. Cerrahi ile çıkarılabilir. Takip veya müdahale için bir nöroşirürji uzmanına başvurmanız önerilir."
    elif pred_class == "pituitary":
        return "Tespit edilen tümör türü: HİPOFİZ TÜMÖRÜ. Beynin alt kısmında bulunan hipofiz bezinden kaynaklanır. Hormon bozukluklarına ve görme problemlerine neden olabilir. Erken dönemde endokrinoloji ve nöroşirürji değerlendirmesi gerektirir."
    elif pred_class == "notumor":
        return "Herhangi bir tümör belirtisine rastlanmamıştır. Yine de semptomlarınız devam ediyorsa bir sağlık kuruluşuna başvurmanız önerilir. Bu sonuç sadece görüntüye dayalıdır, kesin tanı için doktor muayenesi gereklidir."
    else:
        return "Sınıf tanımlanamadı. Lütfen sistemi yeniden başlatın veya teknik destek alın."

if __name__ == "__main__":
    app.run(debug=True)
