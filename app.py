from openai import OpenAI
from prompt import prompt_Engineering
from dotenv import load_dotenv
import os
import json
from flask import Flask, render_template, request

# Load environment variables
load_dotenv()
model = os.getenv("MODEL_NAME")
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

# Initialize Flask app
app = Flask(__name__)

# Prompt for OpenAI
prompt = prompt_Engineering()

# Initialize OpenAI client
client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

# Core function to generate CV
def cv_generator(user_input):
    user_input_str = json.dumps(user_input, indent=2)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': "You are an Intelligent CV generator bot."},
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': user_input_str}
        ]
    )
    return response.choices[0].message.content.strip()

# Home route
@app.route('/', methods=['GET', 'POST'])
def get_UserInput():
    cv = None  # Default: no CV yet
    if request.method == 'POST':
        user_input = {
            "Target Job Title": request.form['job_title'],
            "Full Name": request.form['full_name'],
            "Email Address": request.form['email'],
            "Phone Number": request.form['phone'],
            "Location": request.form['location'],
            "LinkedIn Profile": request.form['linkedin'],
            "Portfolio/GitHub": request.form['portfolio'],
            "Skills": request.form['skills'],
            "Education": request.form['education'],
            "Experience": request.form['experience'],
            "Projects": request.form['projects']
        }

        try:
            cv = cv_generator(user_input)
        except Exception as e:
            cv = f"Error: {e}"

    return render_template("index.html", cv=cv)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
