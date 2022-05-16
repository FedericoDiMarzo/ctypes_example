# C-Binding in python
## A simple c-binding example in python with ctypes

This repository contains a simple example to test the c-binding capabilities of python. The module used to realize the binding is called `ctypes.

The **ctypes** binding is based on shared libraries. The process employed to bind c functions with python is the following:

- Compile the c code as a shared library
- Load the shared library in python
- Explicitely define the argument and return types in python
- Call the c function using the `ctypes` module

## Compilation
In order to compile the shared library, just execute the makefile.
```sh
make clean
make
```

Optionally, a 32 bit compilation is provided for testing purposes. The loading of a 32 bit shared library is not supported by **ctypes**

```sh
make clean
make 32bit
```


## Testing the binding

After the shared library has been compiled (in 64 bit format), the binding can be tested by executing the file **c_wrapper.py**

```sh
python3 c_wrapper.py
```

## Numpy binding example

Numpy arrays can be passed as arguments to a c function wrapped with `ctypes` as pointers to contiguous memory areas. Let's consider for example a function definition in c that sums a vector *y* into a vector *x* of the same length *len*.

```c
void sum_vectors(int* x, int* y, int len);
```

Calling `lib` the python object referencing the shared library that includes the `sum_vectors` function, the arguments can be specified as follows.

```python
lib.sum_vectors.argtypes = (
	np.ctypeslib.ndpointer(dtype=int, ndim=1), # x
	np.ctypeslib.ndpointer(dtype=int, ndim=1), # y
	ctypes.c_int # len
)
```

The c function can then be called as follows.

```python
x = np.ones(5)
y = np.ones(5)
lib.sum_vectors(x, y, n)
# x = [2, 2, 2, 2]
```