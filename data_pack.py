import struct


class TLV:

    def __init__(self, type, value):
        self.type = type
        self.value = value
        struct_grammar = '>BBL' if isinstance(self.value, int) else f'>BB{len(self.value)}s'
        if self._value_is_host:
            struct_grammar = '>BB4s'
        self.struct = struct.Struct(struct_grammar)
        self.length = self.struct.size

    @property
    def _value_is_host(self):
        try:
            if len(self.value.split('.')) == 4:
                return True
        except Exception:
            return False

    def _host_to_int(self, host):
        if self._value_is_host:
            self.value = b''
            for i in range(4):
                self.value += struct.pack('>B', int(host.split('.')[i]))

    def pack(self):
        if type(self.value) == str and not self._value_is_host:
            self.value = self.value.encode()
        self._host_to_int(self.value)
        data = self.struct.pack(self.type, self.length, self.value)
        return data


class RadiusDataPack:
    def __init__(self, code, identifier, authenticator, **attributes):
        self.code = code
        self.identifier = identifier
        self.authenticator = authenticator
        self.attributes = attributes
        self._gen_struct()

    def _gen_struct(self):
        struct_format = '>BBH16s'
        for k, v in self.attributes.items():
            struct_format += f'{v.length}s'
        self.struct = struct.Struct(struct_format)
        self.length = self.struct.size

    def _gen_attribute_data(self):
        data_list = []
        for k, v in self.attributes.items():
            data_list.append(v.pack())
        return data_list

    def pack(self):
        data = self.struct.pack(self.code, self.identifier, self.length, self.authenticator,
                                *self._gen_attribute_data())
        print(len(data), data)
        return data
