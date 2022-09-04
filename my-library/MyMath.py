class MyMath:
  @staticmethod
  def range_sum(min_val: int, max_val: int) -> int:
    return (max_val - min_val + 1) * (min_val + max_val) // 2

  @staticmethod
  def div_ceil(divided: int, divisor: int) -> int:
    return (divided + divisor - 1) // divisor
