'''
Table: mm_bg_word_characteristic
Description: Characteristics of the bulgarian words

Field	Type	Null	Default	Comments
id_bg_word 	int(11)	No		Foreign key to “bg_word”
id_characteristic 	int(3)	No		Foreign key to “characteristic”

'''


class MmBgWordCharacteristic:

    def __init__(self):
        self.__id_bg_word = None
        self.__id_characteristic = None

    @property
    def id_bg_word(self):
        return self.__id_bg_word

    @id_bg_word.setter
    def id_bg_word(self, value):
        if self.__id_bg_word is None:
            self.__id_bg_word = value
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
