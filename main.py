import requests
import json

text = input("Text to make clyde say: ")

response = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}")

json_data = json.loads(response.text)

if json_data['status'] == 200 and json_data['success'] == True:
    print("Clyde text successfully generated!")
    print("You can find your text here:")
    input(json_data['message'])
else:
    input("The clyde text had an error. Sorry!")