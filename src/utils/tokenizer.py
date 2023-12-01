from dataclasses import dataclass
from typing import List


@dataclass
class Tokenizer:
    tokens: List[str]

    def to_tokens(self, text: str, *, with_collisions: bool = True) -> List[str]:
        tokens: List[str] = []

        i = 0
        while i < len(text):
            for token in self.tokens:
                if text[i:].startswith(token):
                    tokens.append(token)

                    if not with_collisions:
                        i += len(token) - 1

                    break

            i += 1

        return tokens
