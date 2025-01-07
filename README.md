## Project Overview

This project is an AI agent designed to crawl a website and convert its content into a prompt/answer dataset. It utilizes the OpenRouter API to interact with the `meta-llama/llama-3.1-405b-instruct:free` model for processing the dataset.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**: Set the `OPENROUTER_API_KEY` environment variable with your OpenRouter API key.
   ```bash
   export OPENROUTER_API_KEY='your_api_key_here'
   ```

## Running the Application

To run the application, execute the `main.py` script with the URL of the website you wish to crawl.
```bash
python main.py
```

## OpenRouter API Configuration

Ensure that the `OPENROUTER_API_KEY` environment variable is set correctly. This key is necessary for authenticating requests to the OpenRouter API.

## Examples

### Input
A URL of a website to crawl, e.g., `https://example.com`.

### Output
A dataset of prompt/answer pairs extracted from the website content, processed by the OpenRouter API.

Example:
```json
[
    {
        "prompt": "What is the content of this paragraph?",
        "answer": "This is a sample paragraph content."
    }
]