'''
Table: mm_pl_word_characteristic
Description: Characteristics of the polish words

Field	Type	Null	Default	Comments
id_pl_word 	int(11)	No		Foreign key to “pl_word”
id_characteristic 	int(3)	No		Foreign key to “characteristic”

'''


class MmPlWordCharacteristic:

    def __init__(self):
        self.__id_pl_word = None
        self.__id_characteristic = None

    @property
    def id_pl_word(self):
        return self.__id_pl_word

    @id_pl_word.setter
    def id_pl_word(self, value):
        if self.__id_pl_word is None:
            self.__id_pl_word = value
        else:
            raise Exception('Already has value')

    @property
    def id_characteristic(self):
        return self.__id_characteristic

    @id_characteristic.setter
    def id_characteristic(self, value):
        if self.__id_characteristic is None:
            self.__id_characteristic = value
        else:
            raise Exception('Already has value')
