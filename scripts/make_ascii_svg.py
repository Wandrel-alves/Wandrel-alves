import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"  # Claro -> Escuro

def image_to_ascii(image_path, width=100):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
    
    aspect_ratio = img.shape[0] / img.shape[1]
    height = int(width * aspect_ratio * 0.55) # Ajuste do aspecto do caractere
    img_resized = cv2.resize(img, (width, height))
    
    ascii_lines = []
    num_chars = len(RAMP)
    for row in img_resized:
        line = "".join([RAMP[int((pixel / 255) * (num_chars - 1))] for pixel in row])
        ascii_lines.append(line)
        
    return ascii_lines, width, height

def generate_svg(ascii_lines, width, height, output_path="avi-ascii.svg"):
    font_size = 10
    char_width = 6
    line_height = 12
    
    svg_width = width * char_width
    svg_height = height * line_height

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">',
        '  <style>',
        '    .ascii-text { font-family: monospace; font-size: 10px; fill: #c9d1d9; white-space: pre; }',
        '    @keyframes reveal { from { clip-path: inset(0 100% 0 0); } to { clip-path: inset(0 0 0 0); } }',
        '    .line { animation: reveal 0.1s linear forwards; opacity: 0; animation-fill-mode: forwards; }',
        '  </style>',
        f'  <rect width="100%" height="100%" fill="#0d1117" rx="6"/>',
        f'  <g class="ascii-text">'
    ]

    total_lines = len(ascii_lines)
    for i, line in enumerate(ascii_lines):
        delay = i * 0.04
        # Escapar caracteres HTML no ASCII
        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg.append(
            f'    <text x="10" y="{20 + (i * line_height)}" class="line" '
            f'style="animation-delay: {delay:.2f}s; opacity: 1;">{safe_line}</text>'
        )

    svg.append('  </g>')
    svg.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"SVG criado em: {output_path}")

if __name__ == "__main__":
    try:
        lines, w, h = image_to_ascii("source-prepped.png")
        generate_svg(lines, w, h)
    except Exception as e:
        print(f"Erro: {e}. Certifique-se de executar 'prep_photo.py' antes.")