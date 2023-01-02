# importing the requests library
import requests

def bio_data():
        
    URL="https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()

    print(data)
