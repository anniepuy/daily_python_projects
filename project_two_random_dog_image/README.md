# Project 2: Random Dog Viewer

## Requirements

1. Script that fetches a random dog image URL from the Dog CEO API
2. Parse the response to extract the image URL
3. Download the image and save it locally

## Practice skills

1. Pulling from an API
2. Handling JSON data

## Libraries

1. Requests
   This library helps handle API calls

## How it works & why

1. The first step is to save the API endpoing to a variable called 'image_api'

2. The next step is to create a function that calls the API endpoing, parses the JSON object returned and saves the binary data to a .jpg file locally.

3. There are two API requests. The first one is a get to the API with a status check to make sure the API can return data.

4. The next step is to parse the JSON object to get the image URL

5. The second request is to get the image content from the JSON object. I use the .content attribute because I am getting an image. If I was getting text or HTML, I would use the .text atttribute

6. Next, extract the image file name from the URL using the .split() method

7. Save the binary image to local file. "wb" means to write binary.
