# 🏗️ Construction Content Generator

✨ **AI-Powered Construction Document Engine with Vector Intelligence**

Construction Content Generator is an intelligent system that generates structured construction content using an LLM, converts it into semantic embeddings, stores it inside a FAISS vector database, and delivers the final output as a professionally formatted downloadable PDF.

This system combines AI generation with vector storage to create a scalable construction knowledge pipeline.

---

## 🚀 Project Overview

The system allows users to enter a construction-related topic and automatically:

* 🧠 Generate structured construction content using Gemini 2.5 Flash
* 🔢 Convert generated content into embeddings (all-MiniLM-L6-v2)
* 📦 Store embeddings inside FAISS Vector Database
* 📄 Generate a downloadable PDF document

The platform ensures both **content intelligence and persistent semantic storage**.

---

## 🧠 Workflow Architecture

Based on your Low-Level Design:

```
User Interface
      ↓
Construction Topic Input
      ↓
LLM Model (Gemini 2.5 Flash)
      ↓
Generated Construction Data
      ↓
Embedding Generation (all-MiniLM-L6-v2)
      ↓
FAISS Vector Database Storage
      ↓
Response Generation
      ↓
PDF Creation
      ↓
User Download
```

---

## 🛠️ Tech Stack

| Layer              | Technology                |
| ------------------ | ------------------------- |
| 🧠 LLM             | Gemini 2.5 Flash          |
| 🔢 Embedding Model | all-MiniLM-L6-v2          |
| 📦 Vector Database | FAISS                     |
| 📄 PDF Generation  | Python (ReportLab / FPDF) |
| 🖥️ Interface      | Streamlit                 |
| ⚙️ Backend         | Python                    |

---

## 💡 How It Works

### 1️⃣ User Input

The user enters a construction topic through the interface.

### 2️⃣ LLM Content Generation

Gemini 2.5 Flash generates structured construction content including:

* Technical explanation
* Step-by-step procedures
* Safety guidelines
* Key construction insights

### 3️⃣ Embedding Generation

The generated text is converted into high-dimensional vectors using:

* **all-MiniLM-L6-v2**

### 4️⃣ Vector Database Storage

The embeddings are stored in:

* **FAISS Vector Database**

This enables semantic indexing of construction knowledge.

### 5️⃣ PDF Generation

The final structured content is converted into a downloadable PDF file for the user.

---

## 📄 Output

The system produces:

✔ Structured construction document
✔ Clean formatted PDF
✔ Download button for user
✔ Vector-stored semantic representation of content

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Armibhawsar/Construction-Content-Generator.git
cd Construction-Content-Generator
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Key Features

* AI-powered construction content generation
* Semantic embedding creation
* FAISS vector storage
* Structured document formatting
* One-click PDF download
* Clean and modular architecture

---

## 📈 Use Cases

✔ Construction project documentation
✔ Safety manuals generation
✔ Technical report automation
✔ Site procedure documentation
✔ Client-ready PDF generation

---


