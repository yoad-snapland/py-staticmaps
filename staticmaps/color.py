import random
import re
import typing

ColorT = typing.Tuple[float, float, float]


def parse_color(s: str) -> ColorT:
    re_rgb = re.compile(r"^(0x|#)([a-f0-9]){6}$")

    s = s.strip().lower()

    m = re_rgb.match(s)
    if m:
        v = int("0x" + m[2], 16)
        return (
            ((v << 16) & 0xFF) / 0xFF,
            ((v << 8) & 0xFF) / 0xFF,
            (v & 0xFF) / 0xFF,
        )

    color_map = {
        "black": (0.0, 0.0, 0.0),
        "blue": (0.0, 0.0, 1.0),
        "brown": (0x96 / 0xFF, 0x4B / 0xFF, 0.0),
        "green": (0.0, 1.0, 0.0),
        "orange": (1.0, 0.5, 0.0),
        "purple": (0.5, 0.0, 0.5),
        "red": (1.0, 0.0, 0.0),
        "yellow": (1.0, 1.0, 0.0),
        "white": (1.0, 1.0, 1.0),
    }
    if s in color_map:
        return color_map[s]

    raise ValueError("Cannot parse color string: {}".format(s))


def text_color(color: ColorT) -> ColorT:
    (r, g, b) = color
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return (0.0, 0.0, 0.0) if luminance >= 0.5 else (1.0, 1.0, 1.0)


def random_color() -> ColorT:
    return random.choice(
        [
            (0.0, 0.0, 0.0),
            (0.0, 0.0, 1.0),
            (0x96 / 0xFF, 0x4B / 0xFF, 0.0),
            (0.0, 1.0, 0.0),
            (1.0, 0.5, 0.0),
            (0.5, 0.0, 0.5),
            (1.0, 0.0, 0.0),
            (1.0, 1.0, 0.0),
            (1.0, 1.0, 1.0),
        ]
    )