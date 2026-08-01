"""
MARF Script Generator
Generate Bengali reel script using OpenAI.
"""

from openai import OpenAI

from src.config import AI


class ScriptGenerator:
    def __init__(self):
        self.client = OpenAI()

    def generate(self, title: str, summary: str) -> str:
        prompt = f"""
তুমি একজন বাংলা ভিডিও স্ক্রিপ্ট রাইটার।

নিচের আর্টিকেল থেকে ৬০ সেকেন্ডের একটি আকর্ষণীয় Facebook Reel / YouTube Shorts স্ক্রিপ্ট তৈরি করো।

শিরোনাম:
{title}

আর্টিকেল:
{summary}

নিয়ম:
- বাংলা ভাষা
- ১৫০-১৮০ শব্দ
- প্রথম ৩ সেকেন্ডে শক্তিশালী Hook
- শেষে Call To Action
- কোনো Markdown নয়
"""

        response = self.client.chat.completions.create(
            model=AI.get("model", "gpt-5.5"),
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional Bengali script writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8
        )

        return response.choices[0].message.content.strip()


if __name__ == "__main__":
    generator = ScriptGenerator()

    script = generator.generate(
        "ডেমো শিরোনাম",
        "এটি একটি ডেমো আর্টিকেলের সারাংশ।"
    )

    print(script)
