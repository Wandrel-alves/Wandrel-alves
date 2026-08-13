import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path, output_path="source-prepped.png"):
    print(f"Processando imagem: {input_path}...")
    
    # 1. Remover Fundo
    with open(input_path, 'rb') as i:
        input_data = i.read()
        subject = remove(input_data)
    
    # Converter para PIL Image
    img_pil = Image.open(io.BytesIO(subject)).convert("RGBA")
    
    # Criar fundo branco
    background = Image.new("RGBA", img_pil.size, (255, 255, 255))
    alpha_composite = Image.alpha_composite(background, img_pil).convert("L")
    
    # 2. Aplicar CLAHE (Contraste Adaptativo via OpenCV)
    img_np = np.array(alpha_composite)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_np)
    
    # Salvar resultado
    cv2.imwrite(output_path, enhanced)
    print(f"Imagem salva em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/prep_photo.py <caminho_da_foto.jpg>")
    else:
        prep_photo(sys.argv[1])