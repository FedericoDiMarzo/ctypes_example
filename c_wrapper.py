import ctypes
from pathlib import Path

# loading the shared library
LIB_PATH = Path(__file__).parent / "libfoo.so"
SHARED_LIB = ctypes.CDLL(LIB_PATH)

# setting up the types
def setup_types(lib):
    lib.summing.argtypes = (ctypes.c_int, ctypes.c_int)

setup_types(SHARED_LIB)


def summing(x:int, y:int) -> int:
    """ Sums two integer numbers.

    Parameters
    ----------
    x : int
        First number.
    y : int
        Second number.

    Returns
    -------
    int
        Sum of x and y.
    """
    return SHARED_LIB.summing(x, y)

if __name__ == "__main__":
    z = summing(10, 32)
    print(z)