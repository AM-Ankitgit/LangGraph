from langchain_community.document_loaders import WebBaseLoader
url = "https://github.com/campusx-official/langchain-document-loaders/blob/main/webbase_loader.py"
# url = "https://www.cricbuzz.com/"
# doc = WebBaseLoader(url)

url2 = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader([url,url2])
print(loader.load())