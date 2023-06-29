import requests
import argparse
import os

# take the prompt from user 
parser = argparse.ArgumentParser()
parser.add_argument('prompt',help="The prompt to send to the OpenAI Api")
parser.add_argument("file_name",help="Name of the file to save Python script")
args=parser.parse_args()

api_endpoint ='https://api.openai.com/v1/completions'
api_key=os.getenv("OPENAI_API_KEY")
#openai api 


request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
request_data={
  "model": "text-davinci-003",
  "prompt":f"write python script to ${args.prompt}. Provide only code, no text" ,
  "max_tokens": 4000,
  "temperature": 0.5,

 
}
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if(response.status_code==200):
    response_text=response.json()['choices'][0]['text']
    with open(f"{args.file_name}.py",'w') as file:
        file.write(response_text)
else:
    print(f"Request failed with status code : {str(response)}")    