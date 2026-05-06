def uint(val: int | None) -> int | None:
    if not isinstance(val, int) or val < 0:
        return
    return val


def usec_to_seconds(val: float | None) -> float | None:
    if not isinstance(val, (float, int)):
        return
    return val / 1_000_000


def usec_to_seconds_as_int(val: float | None) -> int | None:
    if not isinstance(val, (float, int)):
        return
    return int(val / 1_000_000)
