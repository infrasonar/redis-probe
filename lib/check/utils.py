def uint(val: int | None) -> int | None:
    if not isinstance(val, int) or val < 0:
        return
    return val


<<<<<<< HEAD
def usec_to_seconds(val: int | None) -> float | None:
    if not isinstance(val, int):
=======
def usec_to_seconds(val: float | None) -> float | None:
    if not isinstance(val, (float, int)):
>>>>>>> 139e092b875685c1126e0e9629a51daa6896f327
        return
    return val / 1_000_000


<<<<<<< HEAD
def usec_to_seconds_as_int(val: int | None) -> int | None:
    if not isinstance(val, int):
=======
def usec_to_seconds_as_int(val: float | None) -> int | None:
    if not isinstance(val, (float, int)):
>>>>>>> 139e092b875685c1126e0e9629a51daa6896f327
        return
    return int(val / 1_000_000)
