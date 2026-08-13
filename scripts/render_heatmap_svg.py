import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_svg(output_path="contrib-heatmap.svg"):
    try:
        with open("data/contributions.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Arquivo json não encontrado. Usando fetch_contributions.py para baixar os dados é necessário!")
        return

    box_size = 12
    gap = 4
    width = 900
    height = 200

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        '    .bg { fill: #0d1117; rx: 12px; stroke: #30363d; stroke-width: 1px; }',
        '    .day { rx: 3px; transform-origin: center; animation: pulseReveal 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; opacity: 0; }',
        '    .day:hover { stroke: #fff; stroke-width: 1px; z-index: 10; }',
        '    @keyframes pulseReveal { ',
        '        0% { opacity: 0; transform: scale(0) translateY(10px); }',
        '        50% { opacity: 1; transform: scale(1.3) translateY(-2px); fill: #58a6ff; }',
        '        100% { opacity: 1; transform: scale(1) translateY(0); }',
        '    }',
        '    .text-title { font: bold 15px "Fira Code", monospace; fill: #c9d1d9; animation: fadeIn 1s ease-in forwards; opacity: 0; }',
        '    .text-sub { font: 12px "Fira Code", monospace; fill: #8b949e; animation: fadeIn 1.5s ease-in forwards; animation-delay: 0.5s; opacity: 0; }',
        '    @keyframes fadeIn { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: translateX(0); } }',
        '  </style>',
        '  <rect width="100%" height="100%" class="bg"/>',
        '  <text x="30" y="30" class="text-title">>_ ACTIVITY RADAR // WANDREL ALVES</text>',
        '  <text x="30" y="50" class="text-sub">Inicializando rastreamento de contribuições em tempo real...</text>',
        '  <g transform="translate(30, 75)">'
    ]

    for i, day in enumerate(data):
        week = i // 7
        dow = i % 7  
        
        x = week * (box_size + gap)
        y = dow * (box_size + gap)
        
        color = PALETTE[min(day.get("level", 0), len(PALETTE) - 1)]
        
        # Criação da "onda" diagonal da animação
        delay = (week * 0.035) + (dow * 0.05) + 0.5

        svg.append(
            f'    <rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
            f'fill="{color}" style="animation-delay: {delay:.3f}s;" />'
        )

    svg.append('  </g>')
    svg.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Heatmap Criativo gerado em: {output_path}")

if __name__ == "__main__":
    render_svg()