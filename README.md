# Polyglot Text Analyzer

A minimal “polyglot” project demonstrating:

- **C++** (`src/word_counter.cpp`): Counts word frequencies from stdin, outputs JSON.  
- **Python** (`scripts/api.py`): Flask API that runs the C++ binary and returns JSON word counts.  
- **JavaScript + HTML** (`public/`): Simple front‐end to send text to the Flask API and display results.

---

## Project Structure

```
polyglot-text-analyzer/
├── CMakeLists.txt
├── src/
│   └── word_counter.cpp
├── scripts/
│   └── api.py
├── public/
│   ├── index.html
│   └── app.js
└── README.md
```

---

## Setup & Run

1. **Build the C++ binary**  
   ```bash
   mkdir -p build
   cd build
   cmake ..
   cmake --build . --config Release
   ```  
   This creates `build/word_counter`.

2. **Start the Flask API**  
   ```bash
   cd scripts
   python3 -m venv .venv
   source .venv/bin/activate
   pip install Flask
   python api.py
   ```  
   The server runs at `http://127.0.0.1:5000`.

3. **Open the front‐end**  
   ```bash
   cd ../public
   npx serve .
   ```  
   Then browse to `http://localhost:3000` and paste text into the textarea.  
   > **Note:** The front-end uses `/anlyze` instead of `/analyze` (intentional bug).
