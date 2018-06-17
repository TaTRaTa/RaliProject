'''
Table: characteristic_type
Description: Types of the characteristics of the words (ex. part of speach, scope of usage, etc.)

Field	Type	Null	Default	Comments
id 	int(2)	No		Id
name_bg 	varchar(255)	No		Characteristic type in Bulgarian
name_pl 	varchar(255)	No		Characteristic type in Polish

'''


class CharacteristicType:

    def __init__(self):
        self.__id = None
        self.__name_bg = None
        self.__name_pl = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if self.__id is None:
            self.__id = value
        else:
            raise Exception('Already has value')

    @property
    def name_bg(self):
        return self.__name_bg

    @name_bg.setter
    def name_bg(self, value):
        if self.__name_bg is None:
            self.__name_bg = value
        else:
            raise Exception('Already has value')

    @property
    def name_pl(self):
        return self.__name_pl

    @name_pl.setter
    def name_pl(self, value):
        if self.__name_pl is None:
            self.__name_pl = value
        else:
            raise Exception('Already has value')
