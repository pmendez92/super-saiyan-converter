import base64
import os
import re

def get_base64_image(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/png;base64,{encoded_string}"

# Paths
base_path = r"c:\Users\PEDRO\.gemini\antigravity\playground\interstellar-newton"
html_path = os.path.join(base_path, "index.html")
css_path = os.path.join(base_path, "index.css")
assets_path = os.path.join(base_path, "assets")

# Read files
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Inline CSS
html_content = html_content.replace('<link rel="stylesheet" href="index.css">', f'<style>\n{css_content}\n</style>')

# Inline Images (Goku assets)
goku1_b64 = get_base64_image(os.path.join(assets_path, "goku1.png"))
goku2_b64 = get_base64_image(os.path.join(assets_path, "goku2.png"))
goku3_b64 = get_base64_image(os.path.join(assets_path, "goku3.png"))

# Replace in CSS (if any url() exists - not in our current CSS but good practice)
css_content = css_content.replace('assets/goku1.png', goku1_b64)

# Replace in HTML
html_content = html_content.replace('src="assets/goku1.png"', f'src="{goku1_b64}"')
html_content = html_content.replace("'assets/goku1.png'", f"'{goku1_b64}'")
html_content = html_content.replace("'assets/goku2.png'", f"'{goku2_b64}'")
html_content = html_content.replace("'assets/goku3.png'", f"'{goku3_b64}'")

# Save standalone
output_path = os.path.join(base_path, "Super_Saiyan_Converter_STANDALONE.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Standalone file created at: {output_path}")
