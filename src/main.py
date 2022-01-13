from flask import Flask, json, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec
import lendo_images

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Read OCR API')
spec.register(app)

@app.route("/read_ocr", methods=["POST"])
def read_ocr():
    recibo_details = request.get_json()
    imagem = recibo_details["foto_recibo"]
    #print(imagem)
    resultado = lendo_images.read_image(1, imagem)
    print(resultado)

    return jsonify(resultado)

if __name__ == "__main__":

    app.run(port=6000)