from openai import OpenAI
import yaml

class ChatGptClient:

    def __init__(self):
        with open('application.yaml', 'r') as file:
            yamlFields = yaml.full_load(file)

        self.client = OpenAI(api_key=yamlFields.get("openAIKey"))

    def make_call(self):
        promptString = "I am a software engineer with 3 years of experience. I have a Bachelor's degree in Computer Engineering, and am proficient in Java, Python, C++, and Swift. Would I be a strong applicant for job with this description? "

        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": promptString
                }
            ]
        )

        print(completion.choices[0].message.content)
