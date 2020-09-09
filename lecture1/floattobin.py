#https://stackoverflow.com/questions/51179116/ieee-754-python
import struct
def float_to_bin(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:032b}".format(bits)


def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]


# Driver code
binary =float_to_bin(0.055)
floating =bin_to_float(binary)
print(binary)
print(floating)
