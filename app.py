import boto3
import base64
from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

app = Flask(__name__)

@app.route('/hoja1-201114336', methods=['POST'])
def recognize_text():
    # Obtener la imagen en base64 desde la solicitud POST
    img_base64 = request.json['image']
    # Decodificar la imagen en base64 a bytes
    img_data = base64.b64decode(img_base64)

    # Instanciar el objeto client para utilizar rekognition
    client = boto3.client('rekognition',region_name=AWS_REGION_NAME,
                           aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Obtenemos respuesta de AWS
    response = client.detect_labels(Image={'Bytes': img_data})

    # Obtenemos labels
    label_detections = response['Labels']

    # Retornamos respuesta
    return label_detections

if __name__ == '__main__':
    app.run()
