!pip install openai==0.28

import openai
import os

#Set the API key here
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            #{"role": "system", "content": "You are an expert medical professional and Somebody who can help people with general medical queries and guide them to a correct medical professional  "},
            {"role": "system", "content": "You are a microsoft dot net core expert and you will help developers to build web application and any dotnet application"},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Example chat interaction
user_input = input("")
bot_response = chatbot(user_input)
print(f"Chatbot: {bot_response}")

import streamlit as st
import openai

# Function to query GPT API
def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app starts here
def main():
    st.title("GPT Chatbot")
    st.write("Enter your question below:")

    # Input text box for user
    user_input = st.text_input("You:", "")

    # Button to send input to chatbot
    if st.button("Submit"):
        if user_input:
            # Call the chatbot function
            response = chatbot(user_input)
            st.write(f"Chatbot: {response}")
        else:
            st.write("Please enter a message.")

# Set up your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Run the main function
if __name__ == "__main__":
    main()
