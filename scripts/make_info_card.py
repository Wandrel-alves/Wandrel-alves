import os

def create_info_card():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="220" viewBox="0 0 490 220">
  <style>
    .bg { fill: #0d1117; rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }
    .text { font-family: 'Fira Code', 'Courier New', monospace; font-size: 13px; }
    .title { fill: #58a6ff; font-weight: bold; }
    .prompt { fill: #7ee787; font-weight: bold; }
    .label { fill: #8b949e; }
    .val { fill: #c9d1d9; }
    .highlight { fill: #ffa657; }
  </style>

  <rect width="100%" height="100%" class="bg" />

  <text x="20" y="30" class="text prompt">Wandrel-alves@github <tspan fill="#8b949e">~ $</tspan> <tspan class="title">neofetch</tspan></text>
  <line x1="20" y1="42" x2="470" y2="42" stroke="#21262d" stroke-width="1" />

  <text x="20" y="65" class="text label">OS: <tspan class="val">GitHub Workspace x86_64</tspan></text>
  <text x="20" y="85" class="text label">Host: <tspan class="val">Olá! Sou o Wandrel Alves 👋</tspan></text>
  <text x="20" y="105" class="text label">Foco: <tspan class="highlight">Desenvolvimento Web &amp; Python</tspan></text>
  <text x="20" y="125" class="text label">Status: <tspan class="val">Programando e aprendendo coisas novas ☕</tspan></text>
  
  <text x="20" y="155" class="text label">Tech Stack:</text>
  <text x="20" y="180" class="text">
    <tspan fill="#4584b6">● Python</tspan>  
    <tspan fill="#e34c26">● HTML5</tspan>  
    <tspan fill="#264de4">● CSS3</tspan>  
    <tspan fill="#f0db4f">● JavaScript</tspan>  
    <tspan fill="#f14e32">● Git</tspan>
  </text>
  
  <text x="20" y="202" class="text prompt">Wandrel-alves@github <tspan fill="#8b949e">~ $</tspan> <tspan fill="#7ee787">_</tspan></text>
</svg>"""

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Card gerado em: info-card.svg")

if __name__ == "__main__":
    create_info_card()