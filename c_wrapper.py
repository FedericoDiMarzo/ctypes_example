import ctypes
import numpy as np
from pathlib import Path

# loading the shared library
LIB_PATH = Path(__file__).parent / "libfoo.so"
SHARED_LIB = ctypes.CDLL(LIB_PATH)

# structure wrappers
class Cpx(ctypes.Structure):
    """ Wrapper to the c cpx structure. """
    _fields_ = [
        ("r", ctypes.c_float),
        ("i", ctypes.c_float),
    ]

    def __str__(self,) -> str:
        return f"{self.r} - {self.i}"


# setting up the types
def setup_types(lib):
    lib.summing.argtypes = (ctypes.c_int, ctypes.c_int)
    lib.summing.restype = ctypes.c_int

    lib.sum_vectors.argtypes = (
        np.ctypeslib.ndpointer(dtype=int, ndim=1, flags='C_CONTIGUOUS'),
        np.ctypeslib.ndpointer(dtype=int, ndim=1, flags='C_CONTIGUOUS'),
        ctypes.c_int
    )

    lib.sum_cpx.argtypes = (Cpx, Cpx)
    lib.sum_cpx.restype = Cpx


setup_types(SHARED_LIB)



def summing(x: int, y: int) -> int:
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


def sum_vectors(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Sums the vector y into x.

    Parameters
    ----------
    x : np.ndarray
        Accumulator vector of shape (n).
    y : np.ndarray
        Vector summed to x of shape (n)

    Returns
    -------
    np.ndarray
        Return x after y is summed to it.
    """
    assert x.shape[0] == y.shape[0], "x and y must have the same length"

    # lenght of the vectors
    n = x.shape[0]

    SHARED_LIB.sum_vectors(x, y, n)
    return x

def sum_cpx(x:Cpx, y:Cpx)->Cpx:
    """
    Summs two complex numbers.

    Parameters
    ----------
    x : Cpx
        First complex number.
    y : Cpx
        Second complex number.

    Returns
    -------
    Cpx
        Sum of x and y.
    """
    return SHARED_LIB.sum_cpx(x,y)

if __name__ == "__main__":
    print(summing(10, 32))

    print(sum_vectors(
        np.array([1, 2, 3]).astype(int),  # x
        np.array([4, 5, 6]).astype(int)  # y
    ))

    print(sum_cpx(Cpx(1,2), Cpx(3,4)))
