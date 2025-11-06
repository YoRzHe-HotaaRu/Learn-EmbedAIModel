# Semantic Similarity Checker

A Flask web application that compares the semantic similarity between two pieces of text using OpenAI's embedding models via the OpenRouter API.

## 🌟 Features

- **Real-time Text Similarity Analysis**: Compare any two pieces of text and get instant similarity scores
- **AI-Powered Embeddings**: Uses OpenAI's text-embedding-3-large model for high-quality semantic understanding
- **Cosine Similarity Calculation**: Implements mathematical similarity scoring (0-100%)
- **Simple Web Interface**: Clean, user-friendly form-based interface
- **API Key Management**: Secure environment variable configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenRouter API key

### Installation

1. **Clone or download this repository**
2. **Install dependencies:**
   ```bash
   pip install flask openai scikit-learn numpy python-dotenv
   ```

3. **Set up your API key:**
   Create a `.env` file in the project root:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:5000`

## 📖 How It Works

1. **Input Text**: Enter two pieces of text you want to compare
2. **Embedding Generation**: The app converts each text into a high-dimensional vector using OpenAI's embedding model
3. **Similarity Calculation**: Uses cosine similarity to measure how similar the meaning of the texts are
4. **Score Display**: Shows a percentage score (0% = completely different, 100% = identical meaning)

## 🏗️ Project Structure

```
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── .env                  # Environment variables (API keys)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Technical Details

### Dependencies

- **Flask**: Web framework for the user interface
- **OpenAI**: API client for embeddings
- **scikit-learn**: Cosine similarity calculations
- **numpy**: Numerical operations
- **python-dotenv**: Environment variable management

### Key Functions

- `get_embedding(text_to_embed)`: Calls OpenRouter API to get text embeddings
- `calculate_similarity(v1, v2)`: Computes cosine similarity between two vectors
- `/compare` route: Handles form submission and returns similarity results

### API Configuration

- **Model**: `openai/text-embedding-3-large`
- **Base URL**: `https://openrouter.ai/api/v1`
- **Request Headers**: Includes optional referer and title for API usage tracking

## 🛡️ Security Notes

- Your OpenRouter API key should be kept secret and stored in the `.env` file
- The `.gitignore` file prevents accidental commits of sensitive files
- Never share your API key or commit the `.env` file to version control

## 🎯 Use Cases

- **Content Comparison**: Check if two articles discuss similar topics
- **Duplicate Detection**: Identify similar content in databases
- **Search Relevance**: Compare query results with intended search terms
- **Plagiarism Detection**: Basic similarity checking for academic work

## 📝 Example Output

```
Similarity Score: 87.32%

(A score of 100% means the meanings are identical. 
0% means they are completely unrelated.)
```

## 🚀 Development

To modify the application:

1. **Edit `app.py`** to change the core logic or add new features
2. **Modify `templates/index.html`** to update the user interface
3. **Update dependencies** in your environment as needed

## 📄 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional similarity metrics
- Batch processing capabilities
- Enhanced UI/UX
- Performance optimizations
- Additional embedding models

---

**Note**: This application requires an active OpenRouter API key with sufficient credits for embedding generation.