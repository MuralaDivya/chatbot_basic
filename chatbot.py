import google.generativeai as genai

# Configure API key
genai.configure(api_key="YOUR_API_KEY"
# Use a valid model from your list
model = genai.GenerativeModel("models/gemini-flash-latest")

print("Gemini Chatbot")
print("Type bye to exit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Gemini: Goodbye 👋")
        break

    response = model.generate_content(user_input)
    print("Gemini:", response.text)
