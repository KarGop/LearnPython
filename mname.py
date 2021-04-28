import requests
import sys

headers = {
    'Content-type': 'application/json',
}
base_url = 'https://2fjmq6ym4i.execute-api.us-east-2.amazonaws.com/prod'

with open('MAC.txt', 'r') as f_input, open('responses.txt', 'w') as f_output:
    for line in f_input:
        search_term = line.strip(' \n\t')
        url = base_url.format(search_term)
        print url
        batch = requests.get(url)
        f_output.write("{},{}\n".format(url, batch.text))
