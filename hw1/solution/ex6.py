import sys


def print_primitive_sizes():
    # int
    print(f"Type: {type(1)}, Value: 1, Size: {sys.getsizeof(1)} bytes")
    print(f"Type: {type(42)}, Value: 42, Size: {sys.getsizeof(42)} bytes")
    print(f"Type: {type(-1)}, Value: -1, Size: {sys.getsizeof(-1)} bytes")
    print(f"Type: {type(0)}, Value: 0, Size: {sys.getsizeof(0)} bytes")
    print(f"Type: {type(100)}, Value: 100, Size: {sys.getsizeof(100)} bytes")

    # float
    print(f"Type: {type(0.0)}, Value: 0.0, Size: {sys.getsizeof(0.0)} bytes")
    print(f"Type: {type(1.0)}, Value: 1.0, Size: {sys.getsizeof(1.0)} bytes")
    print(f"Type: {type(3.14159)}, Value: 3.14159, Size: {sys.getsizeof(3.14159)} bytes")
    print(f"Type: {type(-2.71828)}, Value: -2.71828, Size: {sys.getsizeof(-2.71828)} bytes")
    print(f"Type: {type(2.22507e-308)}, Value: 2.22507e-308, Size: {sys.getsizeof(2.22507e-308)} bytes")

    # complex
    print(f"Type: {type(1+1j)}, Value: 1+1j, Size: {sys.getsizeof(1+1j)} bytes")
    print(f"Type: {type(2+3j)}, Value: 2+3j, Size: {sys.getsizeof(2+3j)} bytes")
    print(f"Type: {type(-1-1j)}, Value: -1-1j, Size: {sys.getsizeof(-1-1j)} bytes")
    print(f"Type: {type(123456789+987654321j)}, Value: 123456789+987654321j, Size: {sys.getsizeof(123456789+987654321j)} bytes")
    print(f"Type: {type(1.1+2.2j)}, Value: 1.1+2.2j, Size: {sys.getsizeof(1.1+2.2j)} bytes")

    # string
    print(f"Type: {type('a')}, Value: 'a', Size: {sys.getsizeof('a')} bytes")
    print(f"Type: {type('abc')}, Value: 'abc', Size: {sys.getsizeof('abc')} bytes")
    print(f"Type: {type('')}, Value: '', Size: {sys.getsizeof('')} bytes")
    print(f"Type: {type('Python')}, Value: 'Python', Size: {sys.getsizeof('Python')} bytes")
    print(f"Type: {type('12345')}, Value: '12345', Size: {sys.getsizeof('12345')} bytes")

    # boolean
    print(f"Type: {type(True)}, Value: True, Size: {sys.getsizeof(True)} bytes")
    print(f"Type: {type(False)}, Value: False, Size: {sys.getsizeof(False)} bytes")

    # NoneType
    print(f"Type: {type(None)}, Value: None, Size: {sys.getsizeof(None)} bytes")


# Call the function
print_primitive_sizes()
