"""
generate.py  – Gemini 1.5 Flash edition
Creates:
  output/questions.json   (raw data)
  output/questions.html   (pretty web report)
  output/questions.csv    (spreadsheet ready)
"""
import json
import csv
import os
from pathlib import Path
import google.generativeai as genai

OUTPUT_DIR     = Path("output")
CONTENT_FILE   = OUTPUT_DIR / "content.json"
QUESTIONS_FILE = OUTPUT_DIR / "questions.json"
HTML_FILE      = OUTPUT_DIR / "questions.html"
CSV_FILE       = OUTPUT_DIR / "questions.csv"

# 1️⃣  Insert your Gemini API key here (or set env-var GEMINI_API_KEY) -> i have not used openai as i reached quota limit :<
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "You_can_paste_your_key_here")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT = """
You are a grade-1 Math teacher.
Given the attached image, create ONE multiple-choice question with exactly 4 options (A, B, C, D).
Return pure JSON only:
{"question":"...","options":["A) ...","B) ...","C) ...","D) ..."],"answer":"C"}
"""

def generate():
    pages = json.loads(CONTENT_FILE.read_text(encoding="utf-8"))
    questions = []

    for page in pages:
        for img_rel in page["images"]:
            img_path = OUTPUT_DIR / img_rel
            if not img_path.exists():
                print("⚠️  missing", img_rel)
                continue
            try:
                img_data = img_path.read_bytes()
                response = model.generate_content(
                    [PROMPT, {"mime_type": "image/png", "data": img_data}]
                )
                text = response.text.strip()
                # remove ```json fences if present
                if text.startswith("```json"):
                    text = text[7:-3]
                data = json.loads(text)
                data["images"] = str(img_rel)
                questions.append(data)
            except Exception as e:
                print("⚠️  error on", img_rel, e)

    # ------------------------------------------------------------------
    # RAW JSON
    # ------------------------------------------------------------------
    QUESTIONS_FILE.write_text(
        json.dumps(questions, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # ------------------------------------------------------------------
    # PRETTY HTML
    # ------------------------------------------------------------------
    html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>IMO Grade-1 Questions</title>
  <style>
    body{{font-family:Segoe UI,Arial;background:#f5f7fa;margin:0;padding:2rem}}
    .card{{display:flex;gap:1rem;background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:1rem;margin-bottom:1rem;box-shadow:0 2px 4px rgba(0,0,0,.05)}}
    img{{max-width:200px;border-radius:4px;object-fit:cover}}
    .meta{{font-size:.9rem;color:#64748b;margin-top:.25rem}}
  </style>
</head>
<body>
  <h1 style="text-align:center">IMO Grade-1 Generated Questions</h1>
  {''.join(
      f'<div class="card">'
      f'<img src="{q["images"]}" loading="lazy">'
      f'<div>'
      f'<p><strong>{q["question"]}</strong></p>'
      + ''.join(f'<div>{opt}</div>' for opt in q["options"]) +
      f'<div class="meta">Answer: <strong>{q["answer"]}</strong></div>'
      f'</div></div>'
      for q in questions
  )}
</body>
</html>
    """.strip()
    HTML_FILE.write_text(html, encoding="utf-8")

    # ------------------------------------------------------------------
    # CSV FOR EXCEL / GOOGLE-SHEETS
    # ------------------------------------------------------------------
    with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Question", "Option A", "Option B", "Option C", "Option D", "Answer", "Image"])
        for q in questions:
            opts = [opt[3:] for opt in q["options"]]  # remove "A) "
            writer.writerow([q["question"], *opts, q["answer"], q["images"]])

    print("✅ JSON  →", QUESTIONS_FILE)
    print("✅ HTML  →", HTML_FILE)
    print("✅ CSV   →", CSV_FILE)

if __name__ == "__main__":
    generate()