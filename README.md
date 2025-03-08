# Gemini AI Projects

This repository contains two projects utilizing Google's **Gemini AI models** for text-based and vision-based responses.

## 📌 Projects Overview

### 1️⃣ Gemini Q&A App (Text-based)
A **Streamlit** web application that allows users to ask questions, and it generates responses using the **Gemini 1.5 Pro** model.

#### 🚀 Features:
- Takes a **textual question** as input.
- Generates a **response** using the `gemini-1.5-pro` model.
- Simple and interactive UI using **Streamlit**.

#### 🛠️ How to Run:
```sh
pip install -r requirements.txt
streamlit run qna_app.py
```

---

### 2️⃣ Gemini Vision App (Text & Image-based)
A **Streamlit** web application that accepts **text prompts and images**, utilizing the **Gemini 2.0 Flash** model for vision-based Q&A.

#### 🚀 Features:
- Accepts **text input** and/or an **image**.
- Uses `gemini-2.0-flash` to generate responses.
- Displays the **uploaded image** with a corresponding AI-generated response.

#### 🛠️ How to Run:
```sh
pip install -r requirements.txt
streamlit run vision_app.py
```

---

## 🔧 Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Abubakar0011/gemini_end-to-end_Q-A_and_Vision_Project.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up API Key:
   - Create a `.env` file in the root directory.
   - Add your Gemini API Key:
     ```sh
     GEMINI_API_KEY=your_api_key_here
     ```

4. Run the applications:
   - For **text-based Q&A:**
     ```sh
     streamlit run qna_app.py
     ```
   - For **vision-based Q&A:**
     ```sh
     streamlit run vision_app.py
     ```

---

## 📦 Project Structure
```
📂 gemini-ai-projects/
├── 📄 qna_app.py          # Gemini 1.5 Pro - Text-based Q&A app
├── 📄 vision_app.py       # Gemini 2.0 Flash - Vision-based app
├── 📄 requirements.txt    # Dependencies list
├── 📄 .env.example        # Example .env file
├── 📄 README.md           # Project documentation (this file)
```

---

## 📌 Dependencies
Ensure you have the following Python packages installed:
```sh
streamlit
google-generativeai
dotenv
pillow
```
Install all dependencies via:
```sh
pip install -r requirements.txt
```

---

## 💡 Future Enhancements
- ✅ Improve UI with better styling.
- ✅ Add support for multiple image uploads.
- ✅ Implement chat history for user interaction.

---

## 🤝 Contribution
Feel free to open issues or pull requests to improve this project!

---

## 📜 License
This project is **MIT licensed**. You are free to use, modify, and distribute it.

