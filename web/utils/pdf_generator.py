from fpdf import FPDF
import os

def generate_pdf(predictions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Beyin Tümörü Tahmin Raporu", ln=True, align='C')
    pdf.ln(10)

    def remove_turkish_characters(text):
        return (text.replace("ı", "i")
                .replace("İ", "I")
                .replace("ş", "s")
                .replace("Ş", "S")
                .replace("ğ", "g")
                .replace("Ğ", "G")
                .replace("ü", "u")
                .replace("Ü", "U")
                .replace("ö", "o")
                .replace("Ö", "O")
                .replace("ç", "c")
                .replace("Ç", "C"))


    for result in predictions:
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 10, remove_turkish_characters(result['filename']), ln=True)
        pdf.cell(0, 10, remove_turkish_characters(result['display_class']), ln=True)
        pdf.cell(0, 10, remove_turkish_characters(result['confidence']), ln=True)
        pdf.multi_cell(0, 10, remove_turkish_characters(result['advice']))
        pdf.ln(5)

    output_path = os.path.join("static", "results", "prediction_report.pdf")
    pdf.output(output_path)
    return output_path
