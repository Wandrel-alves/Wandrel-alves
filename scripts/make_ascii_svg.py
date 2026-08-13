import os

def create_ascii_svg():
    # Arte ASCII em texto no estilo terminal
    ascii_art = [
        "   _  _ _ _____ ___ ___  _   _  ____   ",
        "  | || | |_   _/ __/ _ \\| | | |/ ___|  ",
        "  | || |   | || | | | | | | | | |___   ",
        "  |__   _| | || |_| |_| | |_| |  ___|  ",
        "     |_|   |_| \\___\\___/ \\___/|_|      ",
        "                                       ",
        "   > Wandrel Alves | Developer Profile  ",
        "   > System Status: Online & Coding    "
    ]

    lines_svg = []
    y = 30
    for line in ascii_art:
        line_escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
        lines_svg.append(f'<text x="15" y="{y}" class="ascii">{line_escaped}</text>')
        y += 20

    height = y + 15

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="370" height="{height}" viewBox="0 0 370 {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }}
    .ascii {{ font-family: 'Fira Code', 'Courier New', monospace; font-size: 11px; fill: #7ee787; white-space: pre; font-weight: bold; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  {"".join(lines_svg)}
</svg>"""

    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("ASCII Banner gerado com sucesso em: avi-ascii.svg")

if __name__ == "__main__":
    create_ascii_svg()