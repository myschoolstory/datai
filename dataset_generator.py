from crawler import crawl_website

def format_data_for_ai_model(prompt_answer_pairs):
    """
    Formats the extracted prompt/answer pairs into a structured dataset suitable for the AI model.
    
    :param prompt_answer_pairs: A list of tuples containing prompt/answer pairs.
    :return: A list of dictionaries with 'prompt' and 'answer' keys.
    """
    formatted_dataset = []
    
    for prompt, answer in prompt_answer_pairs:
        formatted_entry = {
            'prompt': prompt,
            'answer': answer
        }
        formatted_dataset.append(formatted_entry)
    
    return formatted_dataset

def generate_dataset(url):
    """
    Generates a prompt/answer dataset from the given website URL.
    
    :param url: The URL of the website to crawl and extract data from.
    :return: A formatted dataset ready for use with the AI model.
    """
    prompt_answer_pairs = crawl_website(url)
    if not prompt_answer_pairs:
        print(f"No data extracted from {url}.")
        return []
    
    formatted_dataset = format_data_for_ai_model(prompt_answer_pairs)
    return formatted_dataset