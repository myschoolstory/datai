import os
from openai import OpenAI

class OpenRouterAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = "https://openrouter.ai/api/v1"

        if not self.api_key:
            raise ValueError("API key for OpenRouter is not set. Please set the OPENROUTER_API_KEY environment variable.")

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def send_request(self, dataset):
        """
        Sends a request to the OpenRouter API with the given dataset.

        :param dataset: A list of dictionaries containing 'prompt' and 'answer' keys.
        :return: The response from the API.
        """
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": item['prompt']
                    },
                    {
                        "type": "text",
                        "text": item['answer']
                    }
                ]
            } for item in dataset
        ]

        try:
            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://github.com/myschoolstory/datai",  # Optional. Site URL for rankings on openrouter.ai.
                    "X-Title": "Datai",  # Optional. Site title for rankings on openrouter.ai.
                },
                model="google/gemini-2.0-flash-thinking-exp:free",
                messages=messages
            )
            return completion.choices[0].message.content
        except Exception as err:
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
            # Assuming the response is a string, return it directly
            return response
        except Exception as e:
            print(f"Error processing the response: {e}")
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