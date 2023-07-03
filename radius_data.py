import struct


class TLV:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        if self.type == 80:
            self.length = 18
            self.struct = struct.Struct('BB16s')
        if isinstance(self.value, int):
            self.struct = struct.Struct('>BBL')
        elif self.value == "127.0.1.1":
            self.struct = struct.Struct('>BB4s')
        else:
            self.value_length = len(self.value)
            self.struct = struct.Struct(f'>BB{self.value_length}s')
        self.length = self.struct.size

    def pack(self):
        if type(self.value) == str:
            temp = self.value
            self.value = self.value.encode()
            if temp == '127.0.1.1':
                self.value = b''
                for i in range(4):
                    self.value += struct.pack('>B', int(temp.split('.')[i]))

        data = self.struct.pack(self.type, self.length, self.value)
        return data


