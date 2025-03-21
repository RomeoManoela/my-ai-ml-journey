import threading
import requests
from bs4 import BeautifulSoup

urls: list[str] = [
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://docs.smith.langchain.com/",
    "https://docs.smith.langchain.com/"
]

def fetch_url(url: str) -> None:
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
    print(soup.title)
threads: list[threading.Thread] = []
for url in urls:
    thread: threading.Thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()



