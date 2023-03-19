import math
from typing import Tuple


def mag_number(info: Tuple[str, int]) -> int:
    """
    Returns the number of magazines a soldier needs given a
    tuple containing the name of a soldier's weapon and
    the number of streets the soldier has to patrol.

    #>>> mag_number(("PT92", 6))
    2
    #>>> mag_number(("M4A1", 6))
    1
    """
    weapons = {"PT92": 17, "M4A1": 30, "M16A2": 30, "PSG1": 5}
    weapon = info[0]
    streets = info[1]
    bullets = streets * 3
    mags = math.ceil(bullets / weapons[weapon])
    return mags



print(mag_number(("PT92", 6)))