from fastapi import UploadFile, File
from core import process_image


async def post(file: UploadFile = File(...)):
    try:
        image_content = await file.read()
        codes = process_image(image_content)
        response = {
            'statusCode': 500,
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
        await file.close()
    return response
