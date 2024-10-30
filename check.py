# Import the Google Generative AI SDK
import google.generativeai as genai
# Import necessary library to store your API key securely
import os

# Set your Google API key
GOOGLE_API_KEY = 'AIzaSyBwXKpzS2syulUlt_OghvgoJkstPsRE70k'  # Replace with your actual key
genai.configure(api_key=GOOGLE_API_KEY)

# Create a GenerativeModel instance
model = genai.GenerativeModel('gemini-pro')

# Generate content
response = model.generate_content("Write a story about a magic backpack.")

# Print the generated text
print(response.text)
