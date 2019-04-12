import ctypes

lib = ctypes.cdll.LoadLibrary("./libtest.so")
cptr = ctypes.POINTER(ctypes.c_char)
lib.myfunc3.argtypes = (cptr, )

lib.myfunc3(b"hello")
for i in range(10):
    lib.myfunc1()
lib.myfunc2()

data=(1,)
print(data)
print(type(data))

cfunc = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

def py_call_back(string):
    print(string)

lib.call_back(cfunc(py_call_back))
