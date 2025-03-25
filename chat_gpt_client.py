from openai import OpenAI
import yaml

class ChatGptClient:

    def __init__(self):
        with open('application.yaml', 'r') as file:
            yamlFields = yaml.full_load(file)

        self.client = OpenAI(api_key=yamlFields.get("openAIKey"))

    def make_call(self, jobDesc):
        promptString = "I am a Software Engineer with 3 years of experience and I have a Bachelor's degree in Computer Engineering along with a minor in Mathematics. I am proficient in the following programming languages and frameworks: Java, Spring Boot, C++, Python, iOS Development, Swift, SQL, Javascript, Typescript, React, Node.js, Next.js, HTML, CSS. Can you please use that information to determine whether I am qualified for the following position? Please provide your response as a simple Yes or No, with a brief 1-2 sentence explanation for your answer and if you have any sort of doubt, you should default to No.  " + jobDesc

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
