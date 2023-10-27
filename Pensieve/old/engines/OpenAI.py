from Pensieve.old.engines import Engine

import openai


class OpenAI(Engine):
    model = "gpt-3.5-turbo-16k"
    system_prompt: dict
    user_prompts = []

    def __init__(self, key: str):
        openai.api_key = key
        pass

    def system(self, prompt: str):
        self.system_prompt = {
            "role": "system",
            "content": prompt
        }

    def user(self, prompt: str):
        self.user_prompts.append({
            "role": "user",
            "content": prompt
        })

    def complete(self):
        messages = [self.system_prompt]
        for prompt in self.user_prompts:
            messages.append(prompt)

        completion_text = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )

        return completion_text
