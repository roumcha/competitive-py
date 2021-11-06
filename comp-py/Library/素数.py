from typing import List, Tuple
from functools import lru_cache


class PrimeNumbers:
  """素数ですか, 素数一覧, 素因数分解"""
  # todo: 素数テーブル、エラトステネスの篩

  cache_size = None

  @staticmethod
  def is_prime(n: int) -> bool:
    """素数ですか - O(√N)\\
    試し割り法"""

    if n == 1:
      return True
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True

  @staticmethod
  @lru_cache(maxsize=cache_size)
  def is_prime_cached(n: int, __i: int = 2) -> bool:
    """素数ですか - O(√N)\\
    試し割り法、再帰によりキャッシュ"""

    if n % __i == 0:
      return False
    elif __i * __i >= n:
      return True
    else:
      return PrimeNumbers.is_prime_cached(n, __i + 1)

  @staticmethod
  def prime_factorize(n: int) -> List[Tuple[int, int]]:
    """素因数分解 - O(√n)\\
    試し割り法。 [ (2,5), (3,1) ] は、 2^5 * 3^1 を表す"""

    def cntdiv_and_quot(divided: int, divisor: int) -> Tuple[int, int]:
      cnt = 0
      while divided % divisor == 0:
        cnt += 1
        divided = divided // divisor
      return cnt, divided

    res: list[Tuple[int, int]] = []
    i = 2
    q = n
    while i * i <= n:
      c, q = cntdiv_and_quot(q, i)
      if c > 0:
        res.append((i, c))
      i += 1
    if q > 1:
      res.append((q, 1))

    return res
