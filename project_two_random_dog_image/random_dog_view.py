import requests

#Dog CEO API
image_api = "https://dog.ceo/api/breeds/image/random"

def get_random_dog_image(image_api):
    try:
        response = requests.get(image_api)
        response.raise_for_status()
        image_url = response.json()['message']
        image_data = requests.get(image_url).content
        filename = image_url.split("/")[-1]
        with open(filename, "wb") as file:
            file.write(image_data)
        return f"Image downloaded and saved as {filename}"
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")



if __name__=="__main__":
    print(get_random_dog_image(image_api))
