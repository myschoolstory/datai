import os
import requests

class OpenRouterAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = "https://api.openrouter.com/v1/models/meta-llama/llama-3.1-405b-instruct:free"

        if not self.api_key:
            raise ValueError("API key for OpenRouter is not set. Please set the OPENROUTER_API_KEY environment variable.")

    def send_request(self, dataset):
        """
        Sends a request to the OpenRouter API with the given dataset.

        :param dataset: A list of dictionaries containing 'prompt' and 'answer' keys.
        :return: The response from the API.
        """
        if not self.api_key:
            print("API key is missing.")
            return None

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(self.base_url, json=dataset, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def process_response(self, response):
        """
        Processes the response from the OpenRouter API.

        :param response: The response object from the API.
        :return: Processed data or error message.
        """
        if not response:
            return "No response received from the API."

        # Example processing logic
        try:
            results = response.get('results', [])
            if not results:
                return "No results found in the response."
            return results
        except KeyError as e:
            print(f"Key error: {e}")
            return "Error processing the response."

# Example usage
if __name__ == "__main__":
    api = OpenRouterAPI()
    dataset = [
        {'prompt': 'What is the content of this paragraph?', 'answer': 'This is a sample answer.'}
    ]
    response = api.send_request(dataset)
    processed_data = api.process_response(response)
    print(processed_data)