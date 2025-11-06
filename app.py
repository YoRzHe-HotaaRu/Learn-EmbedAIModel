import os
from flask import Flask, render_template, request
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv  # <-- ADD THIS IMPORT

load_dotenv() 

# --- Configuration ---
# The script will now load the key from your .env file
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("ERROR: OPENROUTER_API_KEY not found.")
    print("Please create a .env file and add your key.")
    # You might want to exit or raise an error here in a real app
    
# Initialize the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# Initialize the Flask app
app = Flask(__name__)

# --- Helper Functions ---

def get_embedding(text_to_embed):
    """
    Calls the OpenRouter API to get an embedding for the given text.
    """
    try:
        embedding = client.embeddings.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:5000", # Optional, replace with your site
                "X-Title": "Flask Embedding Demo",      # Optional, replace with your site name
            },
            model="openai/text-embedding-3-large",
            input=text_to_embed,
            encoding_format="float"
        )
        # The embedding is a list of floats
        return embedding.data[0].embedding
    except Exception as e:
        print(f"Error getting embedding: {e}")
        return None

def calculate_similarity(v1, v2):
    """
    Calculates the cosine similarity between two embedding vectors.
    """
    # cosine_similarity expects 2D arrays, so we reshape our 1D vectors
    vec1 = np.array(v1).reshape(1, -1)
    vec2 = np.array(v2).reshape(1, -1)
    
    # Calculate and return the score
    similarity_score = cosine_similarity(vec1, vec2)[0][0]
    return similarity_score

# --- Flask Routes ---

@app.route('/')
def index():
    """
    Serves the main HTML page.
    """
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    """
    Handles the form submission, gets embeddings, and calculates similarity.
    """
    # Get text from the form
    text1 = request.form['text1']
    text2 = request.form['text2']

    # 1. Get embedding for Text 1
    print(f"Getting embedding for: {text1}")
    v1 = get_embedding(text1)

    # 2. Get embedding for Text 2
    print(f"Getting embedding for: {text2}")
    v2 = get_embedding(text2)

    score = 0.0 # Default score
    if v1 is not None and v2 is not None:
        # 3. Calculate the similarity
        score = calculate_similarity(v1, v2)
        print(f"Similarity score: {score}")

    # 4. Render the page again, this time with the score
    return render_template('index.html', score=score, text1=text1, text2=text2)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)