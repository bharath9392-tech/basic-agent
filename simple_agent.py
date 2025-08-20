import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- Configuration ---
# Load environment variables from the .env file
load_dotenv()

# Configure the Gemini API with your key
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
except (ValueError, AttributeError) as e:
    print(f"ERROR: Configuration failed. {e}")
    exit()

# --- System Prompt / Persona Definition ---
# Here we define Astra's simple and friendly personality.
SYSTEM_PROMPT = """
You are 'Astra', a friendly and curious AI assistant. 
Your goal is to be a helpful and engaging conversational partner.
Chat with the user in a natural, supportive, and positive way. 
You can discuss any topic the user brings up, from science and technology to art, history, or everyday life.
Keep your responses clear and easy to understand.
"""

# --- Model Initialization ---
# We initialize the model with our defined persona
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    system_instruction=SYSTEM_PROMPT
)

def main():
    """
    Main function to run the chatbot in the terminal.
    """
    # Start a chat session that remembers the conversation
    chat = model.start_chat(history=[])

    print("🤖 Hello! I'm Astra, your friendly AI assistant. What's on your mind today?")
    print("   (Type 'quit' or 'exit' to end our chat)\n")

    while True:
        # Get input from the user
        user_input = input("You: ").strip()

        # Check if the user wants to leave
        if user_input.lower() in ["quit", "exit"]:
            print("\n🤖 It was great chatting with you. Goodbye!")
            break
        
        # Send the message to the model and print the response
        try:
            response = chat.send_message(user_input)
            print(f"\nAstra: {response.text}\n")
        except Exception as e:
            print(f"\nSorry, an error occurred: {e}\nPlease try again.\n")

# --- Run the main function when the script is executed ---
if __name__ == "__main__":
    main()