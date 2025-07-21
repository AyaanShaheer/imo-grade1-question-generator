# 🧒 IMO Grade-1 Question Generator  
### Turn the **official IMO Grade-1 Sample Paper** into beautiful, auto-generated quizzes in **30 seconds** – **100 % free** with **Gemini 1.5 Flash**.

---

## 🎬 Snapshots for EASE:


<img width="1880" height="831" alt="Screenshot 2025-07-21 184507" src="https://github.com/user-attachments/assets/e2bd8232-4b25-4abe-87c8-2e2768c042ff" />


<img width="1868" height="781" alt="Screenshot 2025-07-21 184515" src="https://github.com/user-attachments/assets/0cbdf16e-ae11-450e-949f-531c386de539" />

---

## ✨ Features
| Feature | What you get |
|---------|--------------|
| 📄 **PDF → Questions** | Extracts every image and turns it into a grade-1 MCQ |
| 🤖 **AI Powered** | Google Gemini 1.5 Flash – **no OpenAI credits** |
| 🌐 **Zero Install Hassle** | One `git clone`, one `.env` file → done |
| 🖥️ **Cross-Platform** | Windows / macOS / Linux |
| 📊 **Export Ready** | JSON, HTML (pretty), CSV (Excel) |

---

## 🚀 Quick Start (clone & run)

1. **Clone the repo**
   ```bash
   git clone https://github.com/AyaanShaheer/imo-grade1-question-generator.git
   cd gen_proj
   ```

2. **Create & activate uv environment**
   ```bash
   uv venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

3. **Add your Gemini API key**
   ```bash
   echo "GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE" > .env
   ```
   
4. **Run the Application**
   ```bash
   python execute.py
   python generate.py
   thats it
   ```

---

## 📁 Outputs
| File | Purpose |
|------|---------|
| `output/questions.json` | Raw data for any downstream use |
| `output/questions.html` | **Beautiful, self-contained web page** |
| `output/questions.csv` | Drop straight into Excel or Google Sheets |

---

## 🍴 Fork & Customize

1. **Fork** (GitHub UI → Fork)  
2. **Clone your fork**
   ```bash
   git clone https://github.com/AyaanShaheer/imo-grade1-question-generator.git
   ```
3. **Edit** – change prompts, add new export formats, swap PDFs.  
4. **Push** – your changes stay in your fork without affecting upstream.

---

## 🛠️ Tech Stack
- **Language**: Python 3.11+  
- **Env / Package manager**: `uv` (lightning-fast)  
- **Vision Model**: Google Gemini 1.5 Flash (free tier)  
- **PDF Engine**: PyMuPDF (fitz)  
- **Report**: Pure HTML + CSS (no server, no JS build)

---

## 📜 License
MIT – do whatever you want.

---

## 🤝 Contributing
Pull requests welcome!  
If you add support for other Olympiad grades, open an issue first so we can keep the repo tidy.

---

### ⭐ Star the repo if it helped!
