import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_svg(output_path="contrib-heatmap.svg"):
    try:
        with open("data/contributions.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Execute fetch_contributions.py primeiro!")
        return

    # Layout de 53 semanas x 7 dias
    box_size = 10
    gap = 4
    width = 860
    height = 140

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        '    .bg { fill: #0d1117; rx: 6px; }',
        '    .day { rx: 2px; transform-origin: center; animation: revealDiagonal 0.4s ease-out forwards; opacity: 0; }',
        '    @keyframes revealDiagonal { from { opacity: 0; transform: scale(0); } to { opacity: 1; transform: scale(1); } }',
        '    .text { font: 10px monospace; fill: #8b949e; }',
        '  </style>',
        '  <rect width="100%" height="100%" class="bg"/>',
        '  <g transform="translate(20, 20)">'
    ]

    for i, day in enumerate(data):
        week = i // 7
        dow = i % 7  # Dia da semana (0-6)
        
        x = week * (box_size + gap)
        y = dow * (box_size + gap)
        
        color = PALETTE[min(day["level"], len(PALETTE) - 1)]
        delay = (week + dow) * 0.015 # Animação em fluxo diagonal

        svg.append(
            f'    <rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
            f'fill="{color}" style="animation-delay: {delay:.3f}s;" />'
        )

    # Texto inferior
    svg.append(f'    <text x="0" y="110" class="text">Recent Activity Heatmap</text>')
    svg.append('  </g>')
    svg.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Heatmap gerado em: {output_path}")

if __name__ == "__main__":
    render_svg()