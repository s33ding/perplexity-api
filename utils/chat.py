#!/usr/bin/env python3
"""Perplexity API chat utility."""
import os, sys
from openai import OpenAI

client = OpenAI(api_key=os.environ["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")

def chat(prompt, model="sonar-pro"):
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else input("Prompt: ")
    model = sys.argv[2] if len(sys.argv) > 2 else "sonar-pro"
    print(chat(prompt, model))
