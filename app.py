from flask import Flask, request, jsonify
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    pdf = fitz.open(stream=file.read(), filetype='pdf')

    full_text = []
    for page in pdf:
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang='spa')
        full_text.append(text)

    return jsonify({'text': "\n".join(full_text)})

if __name__ == '__main__':
    app.run(debug=True)
