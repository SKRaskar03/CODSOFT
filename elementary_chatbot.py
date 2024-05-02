import random

# Define some common greetings and farewell messages
greetings = ["Hi there!", "Hello! How can I help you today?"]
farewells = ["Have a great day!", "Thanks for chatting!"]

# Sample knowledge base for FAQs and troubleshooting steps
knowledge_base = {
    "What are your hours of operation?": "We are open Monday-Friday from 9am to 5pm.",
    "How do I return a product?": "Please visit our returns page for instructions: [link to returns page]",
    "How do I contact customer support?":"You Can contact us on Mobile:7845422442,Email-abcsupport@gmail.com"
}

# Function to greet the user
def greet():
    print(random.choice(greetings))

# Function to understand user intent (simple example)
def understand_intent(message):
    keywords = {
        "hours": "What are your hours of operation?",
        "return": "How do I return a product?",
        "support":"How do I contact customer support?"
    }
    lower_message = message.lower()
    for key, value in keywords.items():
        if key in lower_message:
            return value
    return None

# Function to respond to the user
def respond(message):
    intent = understand_intent(message)
    if intent:
        return knowledge_base.get(intent)
    else:
        return "I apologize, I couldn't understand your question. Perhaps you can rephrase it or visit our FAQs page: [link to FAQs page]"

# Function to end the conversation
def end_conversation():
    print(random.choice(farewells))

def main():
    greet()
    while True:
        user_message = input("You: ")
        if user_message.lower() == "goodbye":
            break
        response = respond(user_message)
        if response is not None:
            print("Chatbot: " + response)
        else:
            print("Chatbot: I apologize, I couldn't understand your question. Perhaps you can rephrase it or visit our FAQs page: [link to FAQs page]")
    end_conversation()

if __name__ == "__main__":
    main()
