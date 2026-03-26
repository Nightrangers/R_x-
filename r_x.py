import os
from openai import OpenAI

# 1. Setup the client
# IMPORTANT: Set your OPENAI_API_KEY in your system environment or GitHub Secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Define your Fine-Tuned Model ID 
# Replace this with the ID from your OpenAI Fine-tuning dashboard
MY_MODEL = "ft:gpt-4o-0806:my-org:custom-name:ID" 

def chat_with_model():
    print("AI Chatbot Started! (Type 'quit' to exit)")
    
    # This list keeps track of the conversation history
    messages = [
        {"role": "system", "content": "You are a helpful assistant trained on custom data."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            break

        # Add your message to the history
        messages.append({"role": "user", "content": user_input})

        try:
            # Generate the response using your fine-tuned model
            response = client.chat.completions.create(
                model=MY_MODEL,
                messages=messages,
                temperature=0.7
            )

            # Get the text from the model's response
            answer = response.choices[0].message.content
            print(f"AI: {answer}")

            # Add the AI's response to the history so it remembers the context
            messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_model()
