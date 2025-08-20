import google.generativeai as genai
import os
from dotenv import load_dotenv
import gradio as gr

# --- Configuration (Same as before) ---
load_dotenv()

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")
    genai.configure(api_key=api_key)
except (ValueError, AttributeError) as e:
    print(f"ERROR: Configuration failed. {e}")
    exit()

# --- Persona Definition for Astra (Same as before) ---
SYSTEM_PROMPT = """
You are 'Astra', a friendly and curious AI assistant. 
Your goal is to be a helpful and engaging conversational partner.
Chat with the user in a natural, supportive, and positive way. 
You can discuss any topic the user brings up, from science and technology to art, history, or everyday life.
Keep your responses clear and easy to understand.
"""

# --- Model Initialization ---
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    system_instruction=SYSTEM_PROMPT
)
# We start a chat session that will remember conversation history
chat = model.start_chat(history=[])


# --- Core Chat Function for the GUI ---
def astra_response(message, history):
    """
    This is the function that Gradio will call every time the user sends a message.
    """
    try:
        response = chat.send_message(message)
        return response.text
    except Exception as e:
        return f"Sorry, an error occurred: {e}"


# --- Create and Configure the Gradio Window ---
# This one block of code creates the entire user interface!
demo = gr.ChatInterface(
    fn=astra_response,
    title="🤖 Astra - Your AI Assistant",
    description="Hello! I'm Astra. You can ask me anything or we can just chat. What's on your mind?",
    theme="soft",
    examples=[
        "Explain quantum computing in simple terms",
        "Can you give me a recipe for biryani?",
        "What are some interesting places to visit here in Andhra Pradesh?"
    ]
)

# --- Start the Application ---
if __name__ == "__main__":
    # The launch() command starts the local web server and opens the window.
    demo.launch()