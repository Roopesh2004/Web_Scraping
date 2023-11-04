import requests
import concurrent.futures
import time
import textwrap


wiki_titles = [
    "Python_(programming_language)",
    "Java_(programming_language)",
    "Adipurush",
    "Ram Charan"
]

BASE_URL = "https://en.wikipedia.org/w/api.php"


def fetch_wikipedia_content(title):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "exintro": True,  
        "explaintext": True,  
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))

    content = page.get("extract", "")
    paragraphs = content.split('\n\n')

    print(f"Title: {title.replace('_', ' ')}")
    print("Content:")
    for paragraph in paragraphs:
        formatted_paragraphs = textwrap.fill(paragraph, width=80)
        print(formatted_paragraphs)
        print("\n" + "-" * 80)
    print("\n")


def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(fetch_wikipedia_content, wiki_titles)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
