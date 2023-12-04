from typing import List, TypeVar, Generic

T = TypeVar("T")


def uniq(l: List[T]) -> List[T]:
    """Remove duplicates from a list while preserving order"""
    seen: List[T] = []
    for item in l:
        if item not in seen:
            seen.append(item)

    return seen


def intersect(a: List[T], b: List[T]) -> List[T]:
    return [v for v in a if v in b]


def split_strip(s: str, separator: str) -> List[str]:
    return [n.strip() for n in s.split(separator) if n != ""]
