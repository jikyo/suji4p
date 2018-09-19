#:coding=utf-8:


class Acc():

    def __init__(self):
        self.inside = False
        self.__val = 0
        self.__val_cardinal = 0
        self.__last_cardinal = 10
        self.__base = 10

    def dump(self):
        s = 'Acc:\n'
        s += '\tinside: '			+ str(self.inside)		+ '\n'
        s += '\t__val: '			+ str(self.__val)		+ '\n'
        s += '\t__val_cardinal: '		+ str(self.__val_cardinal)	+ '\n'
        s += '\t__last_cardinal: '		+ str(self.__last_cardinal)	+ '\n'
        s += '\t__base: '			+ str(self.__base)		+ '\n'
        print(s)

    def turn_to_decimal_state(self):
        self.__val = float(self.__val)
        self.__val_cardinal = float(self.__val_cardinal)
        self.__base = float(0.1)

    def attach_cardinal(self, cardinal):
        self.inside = True
        if self.__val is 0:
                self.__val = 1
        if self.__last_cardinal < cardinal:
            self.__val_cardinal = (self.__val_cardinal + self.__val) * cardinal
        else:
            self.__val_cardinal = self.__val_cardinal + (self.__val * cardinal)
        self.__last_cardinal = cardinal
        self.__val = 0

    def attach_number(self, number):
        self.inside = True
        if self.__base < 1:
            self.__val = self.__val  + (float(number) * self.__base)
            self.__base *= 0.1
        else:
            self.__val = (self.__val * self.__base) + number

    def get_value(self):
        return self.__val_cardinal + self.__val


__all__ = [];
