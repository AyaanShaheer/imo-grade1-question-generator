"""
extract.py
Extract text + images from the IMO sample paper and build a JSON
index page-by-page.
"""
import fitz  # PyMuPDF
from pathlib import Path
import json
import base64
from PIL import Image
import io

PDF_FILE = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
OUTPUT_DIR = Path("output")
IMAGES_DIR = OUTPUT_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def extract():
    doc = fitz.open(PDF_FILE)
    pages = []

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        text = page.get_text()
        page_imgs = []

        # 1. Save each image found on this page
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            ext = base_image["ext"]
            img_name = f"page{page_idx+1}_img{img_idx+1}.{ext}"
            img_path = IMAGES_DIR / img_name
            with open(img_path, "wb") as f:
                f.write(img_bytes)

            # Convert to PNG (uniform format)
            png_path = img_path.with_suffix(".png")
            Image.open(img_path).save(png_path, "PNG")
            img_path.unlink()  # delete original
            page_imgs.append(str(png_path.relative_to(OUTPUT_DIR)))

        pages.append({
            "page": page_idx + 1,
            "text": text.strip(),
            "images": page_imgs
        })

    with open(OUTPUT_DIR / "content.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    extract()