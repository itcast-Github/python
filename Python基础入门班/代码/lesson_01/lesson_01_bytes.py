print((1024).to_bytes(2, byteorder = 'big'))
print((65536).to_bytes(8, byteorder = 'little'))
print((-1024).to_bytes(4, byteorder = 'big', signed = True))
print((-1024).to_bytes(4, byteorder = 'little', signed = True))
print((500).to_bytes(2, byteorder = 'big'))
print((3345).to_bytes(2, byteorder = 'big'))    # why \r\x11
print((3124).to_bytes(2, byteorder = 'big'))    # why \x0c4 => \x0c + 4(0x34)
print((3140).to_bytes(2, byteorder ='little'))  # why D\x0c => D(0x44) + 0x0c
print('%x' % 3345)
print('%x' % 3124)
print(0xd11)
print(0xc34)

b = b'china\r\nus'
print(type(b))
s = b.decode()
print(s)
print(s.encode())


# 输出

# b'\x04\x00'
# b'\x00\x00\x01\x00\x00\x00\x00\x00'
# b'\xff\xff\xfc\x00'
# b'\x00\xfc\xff\xff'
# b'\x01\xf4'
# b'\r\x11'
# b'\x0c4'
# b'D\x0c'
# d11
# c34
# 3345
# 3124
# <class 'bytes'>
# china
# us
# b'china\r\nus'
