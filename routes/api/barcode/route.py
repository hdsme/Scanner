from fastapi import UploadFile, File, Form
from pyzbar import pyzbar
import numpy as np
import cv2
import base64
import re


async def post(file: UploadFile = File(None), base_64: str = Form(None)):
    try:
        if file is not None:
            image_content = await file.read()
        else:
            base_64 = re.sub('^data:image\/\w+;base64,', '', base_64)
            image_content = base64.b64decode(base_64)
        nparr = np.frombuffer(image_content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        results = pyzbar.decode(img)
        codes = []
        if (len(results) > 0):
            codes_128 = filter(lambda x: x.type == 'CODE128', results)
            codes = list(map(lambda x: x.data, codes_128))
        response = {
            'statusCode': 200,
            'data': codes,
            'error': None
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'data': [],
            'error': str(e)
        }
    finally:
        if file is not None:
            await file.close()
    return response