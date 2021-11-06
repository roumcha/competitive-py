from typing import Callable


class BinSearch:
  """二分探索"""
  @staticmethod
  def search(ok: int, ng: int, condition: Callable[[int], bool]) -> int:
    """二分探索 - O(log N)\\
    めぐる式二分探索"""
    while abs(ng - ok) > 1:
      mid = (ok + ng) // 2
      if condition(mid):
        ok = mid
      else:
        ng = mid
    return ok
