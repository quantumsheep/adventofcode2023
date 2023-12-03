import re
from collections import OrderedDict
from dataclasses import dataclass
from typing import List


@dataclass
class Token:
    line: int
    column: int

    pattern_type: str
    value: str


class Tokenizer:
    def __init__(
        self,
        *,
        patterns: OrderedDict[str, List[str]],
        ignore_patterns: List[str] = [],
    ):
        self.patterns: OrderedDict[str, List[re.Pattern[str]]] = OrderedDict()
        for pattern_type, patterns in patterns.items():
            self.patterns[pattern_type] = [re.compile(pattern) for pattern in patterns]

        self.ignore_patterns = ignore_patterns

    def to_tokens_simple(
        self, text: str, *, with_collisions: bool = False
    ) -> List[str]:
        tokens = self.to_tokens(text, with_collisions=with_collisions)
        return [token.value for token in tokens]

    def to_tokens(self, text: str, *, with_collisions: bool = False) -> List[Token]:
        tokens: List[Token] = []

        line = 0
        column = 0

        i = 0
        while i < len(text):
            found = False

            for pattern_type, patterns in self.patterns.items():
                for pattern in patterns:
                    # Check if starts with regex
                    match = pattern.match(text[i:])
                    if not match:
                        continue

                    # Get match
                    match = match.group()

                    if pattern_type not in self.ignore_patterns:
                        # Create token
                        token = Token(
                            line=line,
                            column=column,
                            pattern_type=pattern_type,
                            value=match,
                        )
                        tokens.append(token)

                    if not with_collisions:
                        # Update index
                        i += len(match) - 1

                        # Update line and column
                        line_jumps = match.count("\n")
                        if line_jumps > 0:
                            line += line_jumps
                            column = len(match) - match.rfind("\n") - 1
                        else:
                            column += len(match)

                    found = True
                    break

                if found:
                    break

            if not found:
                raise Exception(f"Could not tokenize '{text[i:]}'")

            i += 1

        return tokens
