# C-Binding in python
## A simple c-binding example in python with ctypes

This repository contains a simple example to test the c-binding capabilities of python. The module used to realize the binding is called **ctypes**.

The **ctypes** binding is based on shared libraries. The process employed to bind c functions with python is the following:

- Compile the c code as a shared library
- Load the shared library in python
- Explicitely define the types in python

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
