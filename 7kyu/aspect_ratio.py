from typing import Tuple
import math


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    # 頑張って！
    new_x = math.ceil((16 / 9) * y)
    return new_x, y


print(aspect_ratio(960, 720))
