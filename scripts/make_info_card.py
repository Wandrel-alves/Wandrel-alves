import sys

def create_info_card(output_path="info-card.svg"):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 350" width="490" height="350">
  <style>
    .bg { fill: #0d1117; rx: 6px; }
    .title { font: bold 14px monospace; fill: #58a6ff; }
    .label { font: bold 12px monospace; fill: #79c0ff; }
    .value { font: 12px monospace; fill: #c9d1d9; }
    .fade { animation: fadeIn 0.5s ease-in forwards; opacity: 0; }
    @keyframes fadeIn { to { opacity: 1; } }
  </style>
  <rect width="100%" height="100%" class="bg"/>
  
  <g transform="translate(20, 30)">
    <text y="0" class="title fade" style="animation-delay: 0.1s;">user@github-workspace</text>
    <text y="12" class="value fade" style="animation-delay: 0.2s;">-----------------------</text>
    
    <g transform="translate(0, 40)" class="fade" style="animation-delay: 0.3s;">
      <text class="label">OS:</text><text x="90" class="value">GitHub Profile Terminal v2.0</text>
    </g>
    <g transform="translate(0, 65)" class="fade" style="animation-delay: 0.4s;">
      <text class="label">Role:</text><text x="90" class="value">Software Engineer / Creator</text>
    </g>
    <g transform="translate(0, 90)" class="fade" style="animation-delay: 0.5s;">
      <text class="label">Stack:</text><text x="90" class="value">Python, JavaScript, Docker, Git</text>
    </g>
    <g transform="translate(0, 115)" class="fade" style="animation-delay: 0.6s;">
      <text class="label">Now:</text><text x="90" class="value">Construindo autômatos e SVGs</text>
    </g>
    <g transform="translate(0, 140)" class="fade" style="animation-delay: 0.7s;">
      <text class="label">Highlights:</text><text x="90" class="value">Automações sem servidor &amp; CI/CD</text>
    </g>

    <g transform="translate(0, 180)" class="fade" style="animation-delay: 0.8s;">
      <rect x="0" width="20" height="15" fill="#ff7b72"/>
      <rect x="25" width="20" height="15" fill="#ffa657"/>
      <rect x="50" width="20" height="15" fill="#d2a8ff"/>
      <rect x="75" width="20" height="15" fill="#79c0ff"/>
      <rect x="100" width="20" height="15" fill="#56d364"/>
    </g>
  </g>
</svg>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Card gerado em: {output_path}")

if __name__ == "__main__":
    create_info_card()