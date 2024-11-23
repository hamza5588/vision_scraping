import json

# JSON data as a string
json_data = '''
{
  "company_description": {
    "text": "Our company specializes in innovative solutions for sustainable energy technologies, focusing on integrating advanced materials and software into our systems. We cater to a global clientele ranging from industrial manufacturers to government entities."
  },
  "type_of_operation": "This company operates in the sustainable energy technology sector, developing and integrating advanced materials and software for a variety of clients, including industrial manufacturers and government entities. Due to their focus on advanced materials and industrial manufacturing clients, it is possible that they might have a need for cold finish round bars or require centerless grinding services. These materials and services are often necessary for high-precision manufacturing and the integration of advanced technological solutions.",
  "location": "Barrington, IL, USA",
  "size_of_company_or_revenue": "Based on the provided LinkedIn profile, Swiss Automation, Inc. employs over 300 people. Further revenue details are not provided in the image.",
  "recent_news_or_press_releases": "No recent news or press releases are available based on the provided image of the LinkedIn page.",
  "recent_linkedin_posts": [
    {
      "post": "On behalf of all of us at Swiss Automation, we want to extend our warmest congratulations to each and every one of the West Chicago Football Club players! Your hard work, dedication, and unwavering spirit have led you to this incredible victory of winning your 2nd consecutive championship. We are honored to be part of your journey."
    },
    {
      "post": "Golden Ratio Robotics - WORLD CLASS TEAM #automation&technology #studentinnovation #manufacturingengineering."
    },
    {
      "post": "Congratulations to our Golden Ratio Robotics Team. They are headed to the World Championship in Texas. They beat out 166 teams to get this spot. I am so proud of them!"
    }
  ],
  "insights": "Swiss Automation, Inc. appears to place a strong emphasis on community engagement and support, as evidenced by their congratulations to the West Chicago Football Club for their championship wins. This demonstrates the company's value in team spirit and local involvement. Additionally, the company is actively celebrating its Golden Ratio Robotics Team's recent success in securing a place in the World Championship in Texas, highlighting a commitment to fostering innovation and engineering skills within their team. These achievements could present opportunities to discuss potential partnerships or collaborations in the fields of automation and robotics, which align well with their focus on advanced manufacturing technologies."
}
'''

# Load JSON data
data = json.loads(json_data)

# Prepare formatted text content
formatted_text = ""

# Loop through each key-value pair and format them
for key, value in data.items():
    formatted_text += f"{key}:\n"
    if isinstance(value, list):
        for item in value:
            formatted_text += f"  - {item['post']}\n"
    else:
        formatted_text += f"  {value}\n"
    formatted_text += "\n"

# Write formatted text to a text file
text_file = 'company_data_formatted.txt'
with open(text_file, 'w', encoding='utf-8') as file:
    file.write(formatted_text)

print(f"Text file '{text_file}' has been created successfully.")
