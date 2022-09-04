from typing import List, Tuple, Iterable, TypeVar
from collections import deque
T = TypeVar('T')


class Seq:
  """交互に分ける、連長圧縮、挿入全通り"""

  @staticmethod
  def separate_in_turn(source: Iterable[T], num: int) -> List[List[T]]:
    """交互に分ける - O(N)"""
    source = list(source)
    return [source[i::num] for i in range(num)]

  @staticmethod
  def run_length_encode(source: Iterable[T]) -> List[Tuple[T, int]]:
    """連長圧縮 - O(N)"""
    if not source:
      return []

    src_iter = iter(source)
    res = deque([(next(src_iter), int(1))])

    for item in src_iter:
      prev, prev_cnt = res[-1]
      if item == prev:
        res.pop()
        res.append((prev, prev_cnt + 1))
      else:
        res.append((item, 1))

    return list(res)
