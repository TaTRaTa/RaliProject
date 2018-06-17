'''
Table: characteristic
Description: Characteristics of the words (ex. verb, feminine, botanic, etc.) and their abbreviations

Field	Type	Null	Default	Comments
id 	int(3)	No		Id
abbreviation_bg 	varchar(20)	No		Abbreviation in Bbulgarian
abbreviation_pl 	varchar(20)	No		Abbreviation in Polish
description_bg 	varchar(255)	No		Description in Bulgarian
description_pl 	varchar(255)	No		Description in Polish
description_lat 	varchar(255)	Yes	NULL	Description in Latin
id_characteristic_type 	int(2)	No		Foreign key to “characteristic_type”

'''


class Characheristic:

    def __init__(self):
        self.__id = None
        self.__abbreviation_bg = None
        self.__abbreviation_pl = None
        self.__description_bg = None
        self.__description_pl = None
        self.__description_lat = None
        self.__id_characteristic_type = None

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
    def abbreviation_bg(self):
        return self.__abbreviation_bg

    @abbreviation_bg.setter
    def abbreviation_bg(self, value):
        if self.__abbreviation_bg is None:
            self.__abbreviation_bg = value
        else:
            raise Exception('Already has value')

    @property
    def abbreviation_pl(self):
        return self.__abbreviation_pl

    @abbreviation_pl.setter
    def abbreviation_pl(self, value):
        if self.__abbreviation_pl is None:
            self.__abbreviation_pl = value
        else:
            raise Exception('Already has value')

    @property
    def description_bg(self):
        return self.__description_bg

    @description_bg.setter
    def description_bg(self, value):
        if self.__description_bg is None:
            self.__description_bg = value
        else:
            raise Exception('Already has value')

    @property
    def description_pl(self):
        return self.__description_pl

    @description_pl.setter
    def description_pl(self, value):
        if self.__description_pl is None:
            self.__description_pl = value
        else:
            raise Exception('Already has value')

    @property
    def description_lat(self):
        return self.__description_lat

    @description_lat.setter
    def description_lat(self, value):
        if self.__description_lat is None:
            self.__description_lat = value
        else:
            raise Exception('Already has value')

    @property
    def id_characteristic_type(self):
        return self.__id_characteristic_type

    @id_characteristic_type.setter
    def id_characteristic_type(self, value):
        if self.__id_characteristic_type is None:
            self.__id_characteristic_type = value
        else:
            raise Exception('Already has value')
