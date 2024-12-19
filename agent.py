import os
from openai import OpenAI


class Agent:
    def __init__(self):
        # os.environ["OPENAI_API_KEY"] = ""
        self.client = OpenAI()
    

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": '''You will be provided with a resume or CV of a professional. 
                    Write resolution plan for 2025 (next year) in career focused (more specific with numbers if possible) with following 5 categories that each category has its one or more actions and each action has its description and explaination of why that action is important.
                    Output needs to be in markdown format.
                    Output in English or Mongolian language based on provided resume language. 
                    Only output the resolution.

                    Categories:
                    Personal Growth
                    Career Growth
                    Financial Growth
                    Tech and Hard Skills Growth
                    Soft Skills Growth 
                    '''
                 },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            # temperature=0
        )
        return completion.choices[0].message.content
    

    # def generate_v1(self, info):
    #     prompt = f"{info}"
    #     completion = self.client.chat.completions.create(
    #         model="gpt-4o",
    #         messages=[
    #             {
    #                 "role": "system", "content": '''You will be provided with a resume or CV of a professional. 
    #                 Write resolution plan for 2025 (next year) with following 5 categories. Only output the resolution.
    #                 Output in English or Mongolian language based on provided resume language. 
    #                 1. Personal Growth
    #                 2. Career Growth
    #                 3. Financial Growth
    #                 4. Tech and Hard Skills Growth
    #                 5. Soft Skills Growth 
    #                 '''
    #              },
    #             {
    #                 "role": "user",
    #                 "content": prompt
    #             }
    #         ]
    #     )
    #     return completion.choices[0].message.content