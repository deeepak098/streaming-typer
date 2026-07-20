import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def stream_response(prompt):
    """
    Streams the AI response one chunk at a time.
    """

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        stream=True
    )

    for chunk in stream:

        if chunk.choices:

            content = chunk.choices[0].delta.content

            if content:
                yield content