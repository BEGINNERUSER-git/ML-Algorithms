import urllib.request
import os

URL = "https://storage.googleapis.com/kaggle-data-sets/2243/3960/bundle/archive.zip"
DEST = "data/fashion_mnist.zip"

os.makedirs("data", exist_ok=True)

urllib.request.urlretrieve(URL, DEST)

print("✅ Dataset downloaded. Please unzip it inside /data")
