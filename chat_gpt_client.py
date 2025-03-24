from openai import OpenAI
import yaml

with open('application.yaml', 'r') as file:
    yamlFields = yaml.full_load(file)

client = OpenAI(api_key=yamlFields.get("openAIKey"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content" : "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)