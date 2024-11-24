import base64
import os
# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()
import time

import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from merge import merge_images_vertically
load_dotenv()

secret_key = os.getenv('OPENAI_API_KEY')

options = Options()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/in/messagewaseem/")
time.sleep(10)

try:
    element = driver.find_element(By.CSS_SELECTOR, "#base-contextual-sign-in-modal .contextual-sign-in-modal__modal-dismiss-icon path")
    element.click()
except (ElementNotInteractableException, NoSuchElementException) as e:
    print(f"Error clicking element: {e}")
driver.execute_script("document.body.style.zoom = '60%'")
print("clicked")

# time.sleep(5)

driver.save_screenshot("sebastian4.png")
driver.execute_script("window.scrollTo(0, 2444);")
driver.execute_script("document.body.style.zoom = '60%'")
driver.save_screenshot("sebastian6.png")
driver.quit()


client = OpenAI(api_key=secret_key)

merge_images_vertically("sebastian4.png","sebastian6.png","verticalimage.jpg")
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image("verticalimage.jpg")
# base64_image2 = encode_image("sebastian6.png")

# client = OpenAI(api_key=secret_key)

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# base64_image = encode_image("sebastian6.png")

prompt="""Company Description:
"Our company specializes in innovative solutions for sustainable energy technologies, focusing on integrating advanced materials and software into our systems. We cater to a global clientele ranging from industrial manufacturers to government entities."

Type of Operation:
Using the provided LinkedIn company description, analyze and categorize the type of operation this company runs. Assess whether they might have a need for purchasing cold finish round bars or require centerless grinding services, and provide your reasoning based on their focus areas and clientele.

Location:
Please provide details regarding the company's location.

Size of Company / Revenue:
Based on available information or estimates, describe the size of the company in terms of employee count or revenue.

Recent News or Press Releases:
Find and summarize any recent news or press releases related to this company.

Recent LinkedIn Posts (3):
extract the 3 latest post

find insight:
generate insights based on the collected data, particularly focusing on recent news, press releases, and LinkedIn posts. Using the following recent news articles and LinkedIn posts about a company, generate insights that a salesperson can use during a sales call. Highlight any significant developments, opportunities, or relevant points that could be leveraged in the conversation.
dont include the highlight heading that insight should be in paragrah form

return the responce in csv json"""

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
           {
          "type": "text",
          "text": f"{prompt}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{prompt}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
response_content = response.choices[0].message.content
import json
with open('file.txt', 'w') as f:
    json.dump(response_content, f, indent=2)
print(response_content)

