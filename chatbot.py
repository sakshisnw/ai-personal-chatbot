from transformers import pipeline

chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

def get_response(user_input):
    response = chatbot(user_input)
    return response[0]["generated_text"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
