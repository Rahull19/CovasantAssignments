from langchain.llms.base import LLM
from typing import Optional, List
import requests
import os

class MistralLLM(LLM):
    model: str = "mistral-small"
    temperature: float = 0.7
    api_key: str = os.getenv("MISTRAL_API_KEY")

    @property
    def _llm_type(self) -> str:
        return "mistral_custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature
        }

        response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Mistral API Error: {response.text}")