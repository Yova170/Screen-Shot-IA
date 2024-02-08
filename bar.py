import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def obtener_ultimo_screenshot():
    directorio_screenshots = r"C:\Users\micue\Pictures\Screenshots"

    lista_archivos = os.listdir(directorio_screenshots)

    if not lista_archivos:
        print("No se encontraron archivos en el directorio.")
        return None

    archivo = max((os.path.join(directorio_screenshots, archivo) for archivo in lista_archivos), key=os.path.getctime)
  

    return archivo

def convertir_screenshot_a_texto(ruta_screenshot):
    try:
        imagen = Image.open(ruta_screenshot)
        texto = pytesseract.image_to_string(imagen)

        

        return texto
    except Exception as e:
        print(f"Error al convertir el screenshot a texto: {e}")
        return None

if __name__ == "__main__":
    ruta_ultimo_screenshot = obtener_ultimo_screenshot()

    if ruta_ultimo_screenshot:
        texto_screenshot = convertir_screenshot_a_texto(ruta_ultimo_screenshot)
        

print(texto_screenshot)


from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='es',
    target_language='en',
    timeout=10
)
resultado = translator.translate(texto_screenshot)


import google.generativeai as palm


palm.configure(api_key="AIzaSyCNF0LOsVw_xM-fHIxefvk18TaByUxLEnw")
response = palm.generate_text(prompt= resultado)


translator = EasyGoogleTranslate(
    source_language='en',
    target_language='es',
    timeout=10
)
resultado = translator.translate(response.result)

print(resultado) 