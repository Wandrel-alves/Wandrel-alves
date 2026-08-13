import json
import os

# -------------------------------------------------------------
# 1. GERADOR DO RADAR DE CONTRIBUIÇÕES (contrib-heatmap.svg)
# -------------------------------------------------------------
def make_heatmap():
    PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    
    # Tenta carregar os dados reais, ou gera um mock visual bonito
    try:
        with open("data/contributions.json", "r") as f:
            data = json.load(f)
    except Exception:
        # Dados de exemplo para exibição impecável
        data = [{"level": (i % 5) if (i * 3) % 7 > 2 else 0} for i in range(365)]

    box = 11
    gap = 3
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 170" width="100%">',
        '  <style>',
        '    .bg { fill: #0d1117; rx: 10px; stroke: #30363d; stroke-width: 1px; }',
        '    .title { font: bold 14px "Fira Code", monospace; fill: #58a6ff; }',
        '    .sub { font: 11px "Fira Code", monospace; fill: #8b949e; }',
        '    .radar-line { stroke: #39d353; stroke-width: 1.5px; opacity: 0.4; }',
        '    .day { rx: 2px; }',
        '    .day:hover { stroke: #fff; stroke-width: 1px; }',
        '    @keyframes pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }',
        '    .live-dot { fill: #39d353; animation: pulse 1.5s infinite; }',
        '  </style>',
        '  <rect width="100%" height="100%" class="bg"/>',
        '  <circle cx="25" cy="25" r="4" class="live-dot"/>',
        '  <text x="38" y="29" class="title">WANDREL ALVES // CONTRIBUTIONS RADAR</text>',
        '  <text x="38" y="45" class="sub">Rastreamento de atividade em tempo real • Live Terminal</text>',
        '  <g transform="translate(25, 60)">'
    ]

    for i, day in enumerate(data[:364]):
        week = i // 7
        dow = i % 7
        x = week * (box + gap)
        y = dow * (box + gap)
        color = PALETTE[min(day.get("level", 0), len(PALETTE) - 1)]
        
        # Animação SMIL em onda contínua que nunca para
        begin_delay = (week * 0.03) + (dow * 0.02)
        svg.append(
            f'    <rect class="day" x="{x}" y="{y}" width="{box}" height="{box}" fill="{color}">'
            f'      <animate attributeName="opacity" values="0.2;1;0.8" dur="3s" begin="{begin_delay:.2f}s" repeatCount="indefinite"/>'
            f'    </rect>'
        )

    svg.append('  </g>')
    svg.append('</svg>')

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("✔ contrib-heatmap.svg gerado!")

# -------------------------------------------------------------
# 2. GERADOR DO ASCII ANIMADO EM LOOP (avi-ascii.svg)
# -------------------------------------------------------------
def make_ascii():
    ascii_art = [
        " ┌─────────────────────────────────────────┐",
        " │ >_ DEVELOPER AT WORK                   │",
        " ├─────────────────────────────────────────┤",
        " │  def dev_loop():                        │",
        " │      while True:                        │",
        " │          code_awesome_stuff()           │",
        " │          drink_coffee()                 │",
        " │          git_push_to_main()             │",
        " │                                         │",
        " │  >_ Status: Active & Coding...          │",
        " └─────────────────────────────────────────┘",
        "         \\                             /    ",
        "          \\   .───────────────────.   /     ",
        "           \\  │  (o_  [CODE]  _o) │  /      ",
        "            \\ │  //\\         //\\  │ /       ",
        "             \\'──V_/_───────V_/_──'/        ",
        "              \\___________________/         "
    ]

    lines = []
    y = 28
    for i, line in enumerate(ascii_art):
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
        delay = i * 0.12
        lines.append(
            f'<text x="15" y="{y}" class="ascii-text">'
            f'  <animate attributeName="opacity" values="0;1;1" dur="4s" begin="{delay:.2f}s" repeatCount="indefinite"/>'
            f'  {escaped}'
            f'</text>'
        )
        y += 15

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 410 290" width="100%">
  <style>
    .bg {{ fill: #0d1117; rx: 10px; stroke: #30363d; stroke-width: 1px; }}
    .ascii-text {{
        font-family: 'Fira Code', 'Courier New', monospace;
        font-size: 11px;
        fill: #39d353;
        white-space: pre;
        font-weight: bold;
    }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  {"".join(lines)}
</svg>"""

    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("✔ avi-ascii.svg gerado!")

# -------------------------------------------------------------
# 3. GERADOR DO CARTÃO NEOFETCH (info-card.svg)
# -------------------------------------------------------------
def make_info_card():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 410 290" width="100%">
  <style>
    .bg { fill: #0d1117; rx: 10px; stroke: #30363d; stroke-width: 1px; }
    .text { font-family: 'Fira Code', monospace; font-size: 12px; }
    .title { fill: #58a6ff; font-weight: bold; }
    .prompt { fill: #7ee787; font-weight: bold; }
    .label { fill: #8b949e; }
    .val { fill: #c9d1d9; }
    .highlight { fill: #ffa657; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .cursor { fill: #7ee787; animation: blink 1s infinite; }
  </style>

  <rect width="100%" height="100%" class="bg" />

  <text x="20" y="30" class="text prompt">wandrel@github <tspan fill="#8b949e">~ $</tspan> <tspan class="title">neofetch</tspan></text>
  <line x1="20" y1="42" x2="390" y2="42" stroke="#21262d" stroke-width="1" />

  <text x="20" y="70" class="text label">USER: <tspan class="val">Wandrel Alves</tspan></text>
  <text x="20" y="95" class="text label">ROLE: <tspan class="highlight">Full Stack / Software Developer</tspan></text>
  <text x="20" y="120" class="text label">OS: <tspan class="val">Linux / Windows x86_64</tspan></text>
  <text x="20" y="145" class="text label">STACK: <tspan class="val">Python • JS • HTML5 • CSS3 • Git</tspan></text>
  <text x="20" y="170" class="text label">FOCUS: <tspan class="val">Web Apps &amp; Automation</tspan></text>
  <text x="20" y="195" class="text label">STATUS: <tspan fill="#7ee787">Building cool things ☕</tspan></text>

  <line x1="20" y1="220" x2="390" y2="220" stroke="#21262d" stroke-width="1" />
  <text x="20" y="248" class="text prompt">wandrel@github <tspan fill="#8b949e">~ $</tspan> <rect x="180" y="236" width="8" height="14" class="cursor"/></text>
</svg>"""

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("✔ info-card.svg gerado!")

if __name__ == "__main__":
    make_heatmap()
    make_ascii()
    make_info_card()
    print("\n🎉 Todos os 3 arquivos SVG foram atualizados com sucesso na raiz!")