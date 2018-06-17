'''
Table: mm_bg_word_example_characteristic
Description: Characteristics of the derivations, phrases and examples of the Bulgarian words

Field	Type	Null	Default	Comments
id_bg_word_example 	int(11)	No		Foreign key to “bg_word_example”
id_characteristic 	int(3)	No		Foreign key to “characteristic”

'''


class MmBgWordExampleCharacteristic:

    def __init__(self):
        self.__id_bg_word_example = None
        self.__id_characteristic = None

    @property
    def id_bg_word_example(self):
        return self.__id_bg_word_example

    @id_bg_word_example.setter
    def id_bg_word_example(self, value):
        if self.__id_bg_word_example is None:
            self.__id_bg_word_example = value
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
