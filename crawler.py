import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Sends an HTTP GET request to the specified URL and returns the HTML content.
    
    :param url: The URL of the website to crawl.
    :return: HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    """
    Parses the HTML content using BeautifulSoup and extracts relevant data.
    
    :param html_content: The HTML content to parse.
    :return: A list of extracted data suitable for forming prompt/answer pairs.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    extracted_data = []

    # Example extraction logic: Extract all paragraphs
    for paragraph in soup.find_all('p'):
        text = paragraph.get_text(strip=True)
        if text:
            extracted_data.append(text)

    return extracted_data

def crawl_website(url):
    """
    Crawls the specified website and extracts data to form prompt/answer pairs.
    
    :param url: The URL of the website to crawl.
    :return: A list of prompt/answer pairs.
    """
    html_content = fetch_html(url)
    if not html_content:
        return []

    extracted_data = parse_html(html_content)
    prompt_answer_pairs = []

    # Example logic to form prompt/answer pairs
    for data in extracted_data:
        prompt = f"What is the content of this paragraph?"
        answer = data
        prompt_answer_pairs.append((prompt, answer))

    return prompt_answer_pairs