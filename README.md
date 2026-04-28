# 🏦 FinBot — AI Banking Assistant

An AI-powered customer support chatbot for 
Bank's, specialized in NEFT, RTGS, and 
SFMS payment queries.

## 🚀 Features
- Answers NEFT/RTGS/SFMS banking questions
- Checks transaction status using UTR/Transaction ID
- Handles failed transactions with escalation flow
- Refuses out-of-scope queries (guardrails)
- Never shares customer account details (security)
- Friendly tone with consistent closing message

## 🛠️ Tech Stack
- Python 3.x
- Groq API (LLaMA 3.3 70B model)
- Prompt Engineering (System prompts + Guardrails)
- Google Colab

## 💡 Prompt Engineering Techniques Used
- System Prompts — Define FinBot personality & rules
- Prompt Guardrails — Restrict out-of-scope queries
- Few-shot style instructions — Handle edge cases

## 📋 Sample Interactions

**Customer:** What is minimum RTGS amount?
**FinBot:** Minimum RTGS amount is ₹2,00,000 (2 lakhs)...

**Customer:** Book me a flight ticket
**FinBot:** Booking flights is not my area, but I can 
help with NEFT/RTGS/SFMS queries...

## 🔧 Setup
1. Clone this repository
2. Install dependencies: pip install groq
3. Set your API key: export GROQ_API_KEY=your-key
4. Run: python finbot.py

## 👨‍💻 Author
Charan Sai N — Senior IT Engineer
4+ years experience in IBM WebSphere MQ, 
SFMS, NEFT & RTGS systems
