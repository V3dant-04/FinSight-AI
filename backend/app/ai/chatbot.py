from openai import OpenAI

client = OpenAI()

def finance_chat(context: str, question: str):
    prompt = f"""
You are a personal finance AI assistant.

User financial summary:
{context}
x
User question:
{question}

Give a helpful, short, actionable answer.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
