from abc import ABC, abstractmethod

class LargeLanguageModel(ABC):
    @abstractmethod
    def generate_response(self, prompt, max_tokens, temperature):
        pass