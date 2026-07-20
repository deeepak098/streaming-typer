
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def stream_response(prompt, model="llama-3.3-70b-versatile", temperature=0.7):
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":prompt}],
        temperature=temperature,
        stream=True,
    )

    for chunk in stream:
        try:
            content = chunk.choices[0].delta.content
            if content:
                yield content
        except Exception:
            continue

if __name__ == "__main__":
    prompt = input("Prompt: ")
    print("\nAssistant:\n")
    for token in stream_response(prompt):
        print(token, end="", flush=True)
    print()
