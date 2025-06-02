# Chat with Multiple PDFs

A powerful application that allows you to chat with your PDF documents using AI. Upload multiple PDFs and ask questions about their content - the AI will analyze the documents and provide relevant answers.

## Features

- 📄 Upload and process multiple PDF documents
- 💬 Chat interface for asking questions about the documents
- 🤖 AI-powered responses using OpenAI's language models
- 🔍 Semantic search through document content
- 📱 User-friendly Streamlit interface

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (for embeddings and chat functionality)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/chat-with-pdfs.git
cd chat-with-pdfs
```

2. Create and activate a virtual environment:

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:

```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload your PDF documents using the file uploader in the sidebar

4. Click "Process" to analyze the documents

5. Start asking questions about your documents in the chat interface

## How It Works

The application uses several key technologies:

- **Streamlit**: For the web interface
- **LangChain**: For handling the conversation chain and document processing
- **FAISS**: For efficient vector storage and similarity search
- **OpenAI**: For generating embeddings and powering the chat functionality
- **PyPDF2**: For PDF text extraction

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
