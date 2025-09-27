# 🛍️ ShopAssist AI – Laptop Recommendation Chatbot

ShopAssist AI is an intelligent **laptop recommendation chatbot** built using **Flask** and powered by **OpenAI’s GPT model**.  
It helps users find the best laptop based on their requirements such as performance, portability, display quality, budget, and more.

---

## 📌 Table of Contents
- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [System Design](#-system-design)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [Running the Application](#-running-the-application)
- [Deployment (Flask)](#-deployment-flask)
- [requirements.txt](#-requirementstxt)
- [.env.example](#-envexample)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## 📖 About the Project
In today’s digital age, online shoppers are overwhelmed with **too many choices** and lack personalized assistance.  
ShopAssist AI solves this problem by combining the power of **LLMs** and **rule-based logic** to provide **accurate and personalized laptop recommendations**.

The chatbot:
- Interacts with users conversationally.
- Understands requirements (e.g., GPU, portability, multitasking).
- Recommends the top 3 laptops from a dataset based on preferences.

---

## 🎯 Problem Statement
Given a dataset containing laptop details (name, specifications, description, etc.), build a chatbot that:
1. **Interacts with users** to gather requirements.
2. **Understands laptop needs** (performance, portability, etc.).
3. **Recommends laptops** best suited for the user’s profile.

---

## ✨ Features
- Natural conversation with users using **OpenAI ChatCompletion API**.
- **Multi-stage system**:
  - Stage 1: Intent Clarity & Confirmation.
  - Stage 2: Product Mapping & Information Extraction.
  - Stage 3: Product Recommendation.
- Uses **rule-based scoring** for accurate laptop matching.
- Prevents **LLM hallucinations** with structured outputs (JSON/dictionaries).
- Deployed with **Flask** for easy accessibility.

---

## 🛠️ System Design
The chatbot works in **three stages**:

1. **Intent Clarity & Confirmation**  
   - Collects user needs (budget, GPU, portability, etc.).
   - Stores them in a structured dictionary.

2. **Product Mapping & Information Extraction**  
   - Extracts features from laptop descriptions.  
   - Compares laptop features with user needs using rule-based scoring.  
   - Selects the **top 3 laptops**.

3. **Product Recommendation**  
   - Presents final recommendations.  
   - If no laptops meet criteria → suggests consulting a human expert.

---

## 🧑‍💻 Tech Stack
- **Python 3.12+**
- **Flask** (Backend & Deployment)
- **OpenAI API** (LLM)
- **Pandas** (Data handling)
- **HTML/CSS/JS** (Frontend UI if added)

---

## 📂 Project Structure
ShopAssist-AI/
│── app.py # Flask app entry point
│── requirements.txt # Project dependencies
│── .env.example # Environment variables template
│── static/ # CSS, JS, Images 
│── templates/ # HTML templates (Flask rendering)
│── notebooks/ # Jupyter notebooks (experimentation)
│── data/ # Laptop dataset (CSV)
│── funtions.py/ # Helper functions
│── README.md # Project documentation   
