# Construction-Content-Generator
Construction Content Generator

Generate professional construction site reports automatically using AI.
This project uses Streamlit for the user interface and FPDF for generating PDF reports. Enter a construction topic, and the app produces a formatted, ready-to-download report.

🚀 Features

User-friendly web interface built with Streamlit
AI-powered text generation for construction topics
Automatic PDF report creation with project name and date
Easy to run locally


📂 Project Structure
├── app.py             # Main Streamlit application
├── llm_engine.py      # AI text generation logic
├── prompts.py         # Prompt templates for the AI
├── vector_db.py       # Vector database utilities
├── requirements.txt   # Python dependencies
├── data/              # Project-related documents
└── .gitignore         # Ignores local-only files


⚙️ Installation & Setup

1. Clone the repository
  git clone https://github.com/Armibhawsar/Construction-Content-Generator.git
  cd Construction-Content-Generator

2. Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
      Create a .env file in the project root:
         GOOGLE_API_KEY="your_api_key_here"

▶️ Running the App
   Start the Streamlit app:  streamlit run app.py

📄 Example Usage
      Enter a construction topic, e.g., "Safety protocols for scaffolding."
      The AI generates a professional report automatically.
      Download the report as a PDF file.
