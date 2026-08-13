import os

def create_ascii_svg():
    ascii_art = [
        " ┌─────────────────────────────────────────────────────────────────┐",
        " │ >_ WANDREL ALVES | SOFTWARE DEVELOPER                           │",
        " ├─────────────────────────────────────────────────────────────────┤",
        " │                                                                 │",
        " │  def code_the_future(coffee_cups, ideas):                       │",
        " │      while coffee_cups > 0:                                     │",
        " │          try:                                                   │",
        " │              build_awesome_project(ideas.pop())                 │",
        " │          except BugsFoundException:                             │",
        " │              debug_and_learn()                                  │",
        " │          finally:                                               │",
        " │              coffee_cups -= 1                                   │",
        " │                                                                 │",
        " │      return 'Deploy Successful!'                                │",
        " │                                                                 │",
        " │  >_ System Online. Commencing sequence...                       │",
        " └─────────────────────────────────────────────────────────────────┘",
        "         \\                                                 /       ",
        "          \\     .───────────────────────────────────.     /        ",
        "           \\    │     .-.           .-.             │    /         ",
        "            \\   │    /   \\         /   \\  [====]    │   /          ",
        "             \\  │   |() ()|       |() ()| [====]    │  /           ",
        "              \\ '───\\_=_/─────────\\_=_/─────────────' /            ",
        "               \\_____________________________________/             ",
        "               [_____________________________________]             "
    ]

    lines_svg = []
    y = 30
    for i, line in enumerate(ascii_art):
        line_escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
        delay = i * 0.15 # Efeito de digitação com delay progressivo
        lines_svg.append(
            f'<text x="20" y="{y}" class="ascii-line" style="animation-delay: {delay:.2f}s;">{line_escaped}</text>'
        )
        y += 18

    height = y + 20
    width = 630

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 12px; stroke: #30363d; stroke-width: 1.5px; }}
    .ascii-line {{
        font-family: 'Fira Code', 'Courier New', monospace;
        font-size: 13px;
        fill: #39d353;
        white-space: pre;
        font-weight: bold;
        opacity: 0;
        animation: typeReveal 0.4s ease-out forwards;
    }}
    @keyframes typeReveal {{
        0% {{ opacity: 0; transform: translateX(-15px); }}
        50% {{ opacity: 1; fill: #ffffff; text-shadow: 0 0 5px #39d353; }}
        100% {{ opacity: 1; transform: translateX(0); fill: #39d353; }}
    }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  {"".join(lines_svg)}
</svg>"""

    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("ASCII Code Scene gerado com sucesso em: avi-ascii.svg")

if __name__ == "__main__":
    create_ascii_svg()