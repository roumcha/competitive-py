from typing import List
from functools import lru_cache
import math


class PermAndCombi:
  """階乗(再帰、メモ化), nPr, nCr, パスカルの三角形"""

  cache_size = None

  # modint 使うかもしれないので型ヒント注意
  @staticmethod
  @lru_cache(maxsize=cache_size)
  def fact_cached(n: int) -> int:
    """階乗(再帰、メモ化) - O(n)\\
    21 以上で 64bit 超え"""
    return n * PermAndCombi.fact_cached(n - 1) if n > 1 else 1

  @staticmethod
  def nPr(n: int, r: int) -> int:
    """nPr - O(n)\\
    21 以上で 64bit 超え"""

    if n < r:
      return 0
    res = 1
    for i in range(n - r + 1, n + 1):
      res *= i
    return res

  @staticmethod
  def nCr(n: int, r: int) -> int:
    """nCr - O(n)\\
    21 以上で 64bit 超え"""
    return PermAndCombi.nPr(n, r) // math.factorial(r)

  @staticmethod
  def create_pascalΔ(n: int) -> List[List[int]]:
    """パスカルの三角形 - O(n^2)\\
    66 以上で 64bit 超え"""
    tmp = [[0] * (n+1) for _ in range(n+1)]
    tmp[0][0] = 1

    for i in range(1, n+1):
      for j in range(i+1):
        if j == 0 or j == i:
          tmp[i][j] = 1
        else:
          tmp[i][j] = tmp[i-1][j-1] + tmp[i-1][j]

    return tmp
