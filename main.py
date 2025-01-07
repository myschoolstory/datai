import logging
from crawler import crawl_website
from dataset_generator import generate_dataset
from openrouter_api import OpenRouterAPI

def main(url):
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Step 1: Crawl the website
        logging.info(f"Starting to crawl the website: {url}")
        prompt_answer_pairs = crawl_website(url)
        if not prompt_answer_pairs:
            logging.error("No data extracted from the website.")
            return

        # Step 2: Generate the dataset
        logging.info("Formatting the extracted data into a dataset.")
        dataset = generate_dataset(url)
        if not dataset:
            logging.error("Failed to generate a dataset from the extracted data.")
            return

        # Step 3: Interact with the OpenRouter API
        logging.info("Sending the dataset to the OpenRouter API.")
        api = OpenRouterAPI()
        response = api.send_request(dataset)
        if not response:
            logging.error("No response received from the OpenRouter API.")
            return

        # Step 4: Process and display the response
        logging.info("Processing the response from the OpenRouter API.")
        processed_data = api.process_response(response)
        logging.info(f"Processed data: {processed_data}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example URL to crawl
    example_url = "https://example.com"
    main(example_url)