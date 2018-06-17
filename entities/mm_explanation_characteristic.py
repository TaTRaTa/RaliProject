'''
Table: mm_explanation_characteristic
Description: Characteristics of explanations

Field	Type	Null	Default	Comments
id_explanation 	int(11)	No		Foreign key to “explanation”
id_characteristic 	int(3)	No		Foreign key to “characteristic”

'''


class MmExplanationCharacteristic:

    def __init__(self):
        self.__id_explanation = None
        self.__id_characteristic = None

    @property
    def id_explanation(self):
        return self.__id_explanation

    @id_explanation.setter
    def id_explanation(self, value):
        if self.__id_explanation is None:
            self.__id_explanation = value
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
