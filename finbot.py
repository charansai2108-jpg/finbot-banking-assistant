"""
FinBot — AI Banking Assistant
Author: Charan Sai N
Tech: Python, Groq API, LLaMA 3.3
"""

from groq import Groq
import os

# Load API key safely from environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# FinBot System Prompt
system_prompt = """
You are Charan Sai, a Senior IT Engineer at HDFC 
in Madhapur, Hyderabad. You help customers with 
questions about NEFT, RTGS, SFMS and transaction 
status. Only check transaction status if customer 
provides a valid Transaction ID or UTR number.

If a transaction has failed, ask customer to visit 
nearest branch during working hours or raise a 
support ticket. Our concern team will follow up.

Always respond in a friendly manner.
Never disclose account or contact details of 
any other customers.
Never say no - if you don't know, say 
'I will check and get back to you shortly.'
End every reply with 'Is there anything else 
I can help you?'
"""

def chat_with_finbot(customer_question):
    """Send question to FinBot and get response"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": customer_question}
        ]
    )
    return response.choices[0].message.content

# Test questions
test_questions = [
    "What is the minimum amount for RTGS?",
    "My NEFT transaction TXN2024HYD98765 failed. Help!",
    "Can you book a flight ticket for me?"
]

for question in test_questions:
    print(f"\nCustomer: {question}")
    print(f"FinBot: {chat_with_finbot(question)}")
    print("-" * 50)
