# ShopAssist AI – Laptop Recommendation Chatbot

ShopAssist AI is an intelligent **laptop recommendation chatbot** built using **Flask** and powered by **OpenAI’s GPT model**.  
It helps users find the best laptop based on their requirements such as performance, portability, display quality, budget, and more.

---

## Table of Contents
- [About the Project](#-about-the-project)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [System Design](#-system-design)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [Running the Application](#-running-the-application)
- [requirements.txt](#-requirementstxt)
- [.env.example](#-envexample)
- [Future Enhancements](#-future-enhancements)

---

## About the Project
In today’s digital age, online shoppers are overwhelmed with **too many choices** and lack personalized assistance.  
ShopAssist AI solves this problem by combining the power of **LLMs** and **rule-based logic** to provide **accurate and personalized laptop recommendations**.

The chatbot:
- Interacts with users conversationally.
- Understands requirements (e.g., GPU, portability, multitasking).
- Recommends the top 3 laptops from a dataset based on preferences.

---

## Problem Statement
Given a dataset containing laptop details (name, specifications, description, etc.), build a chatbot that:
1. **Interacts with users** to gather requirements.
2. **Understands laptop needs** (performance, portability, etc.).
3. **Recommends laptops** best suited for the user’s profile.

---

## Features
- Natural conversation with users using **OpenAI ChatCompletion API**.
- **Multi-stage system**:
  - Stage 1: Intent Clarity & Confirmation.
  - Stage 2: Product Mapping & Information Extraction.
  - Stage 3: Product Recommendation.
- Uses **rule-based scoring** for accurate laptop matching.
- Prevents **LLM hallucinations** with structured outputs (JSON/dictionaries).
- Deployed with **Flask** for easy accessibility.

---

## ▶️ Video Demonstration

Watch the 60-second video below to see the complete recommendation process from user input to final output.

https://github.com/user-attachments/assets/6663eacf-0a8a-411f-9553-d0e48fc009d4

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

## Tech Stack
- **Python 3.12+**
- **Flask** (Backend & Deployment)
- **OpenAI API** (LLM)
- **Pandas** (Data handling)
- **HTML/CSS/JS** (Frontend UI)

---

## Project Structure
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

---

## Setup Instructions

Follow these steps to set up the project locally:  
1. **Clone the repository**
- git clone https://github.com/jatinjaglan18/ShopAssistAI.git
- cd ShopAssist-AI

2. **Create Virtual Enviornment**
- python -m venv venv
- source venv/bin/activate    # Mac/Linux
- venv\Scripts\activate       # Windows

3. **Install Dependencies**
- pip install -r requirements.txt

---

## Running the Application
- python app.py
- flask localhost url shown like this - 'http://127.0.0.1:5000'
- Open it 

---

## requirements.txt
- flask - 3.1.2
- openai - 1.109.1
- pandas - 2.3.3
- python-dotenv - 3.12.1`
- ipython - 9.5.0

---

## .env.example
- create .env file
- Put your openai key in .env
  - OPENAI_API_KEY=''  
  
OR
  
- Put your OPENAI api key in the enviornment varible as path    (Best Practice for Security)

---

## Future Enhancements
1. The output format of each layer is inconsistent. You can use the function API capability of GPT to instruct the output format as per the input request.
2. The rule framework provided to classify each laptop’s specification is not exhaustive. You can expand the rules to give a comprehensive context to the LLM.
3. There are misclassifications in the laptop’s specifications, even after specifying clear rules for LLM. You can fine-tune an open-source LLM to make its understanding & performance better.
4. Once the products are extracted, the dialogue flow doesn’t allow recalling of product extraction if there is any intent change. You can add another layer to observe any request for a change in the user intent and then use this flag to recall the product extraction based on the updated intent.
5. As an alternative & simple solution, you can use vector embeddings of each product and compare it with the user intent to find the most relevant products.
6. You can template this workflow/solution to build a chatbot for any product domain. Note: You must add the relevant domain expertise/rules to give the LLM context understanding.
