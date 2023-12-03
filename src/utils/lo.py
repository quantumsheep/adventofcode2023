from typing import List, TypeVar, Generic

T = TypeVar("T")


def uniq(l: List[T]) -> List[T]:
    """Remove duplicates from a list while preserving order"""
    seen: List[T] = []
    for item in l:
        if item not in seen:
            seen.append(item)

    return seen
