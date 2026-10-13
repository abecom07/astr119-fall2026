import requests
import time

url = input("Enter a URL: ")
start = time.time()
response = requests.get(url)
end = time.time()
nbytes = len(response.content)
mbps = (nbytes / (end - start)) / 1000000

print(f"{nbytes} bytes read from {url}")
print(f"Download speed: {mbps:.2f} MB/s")