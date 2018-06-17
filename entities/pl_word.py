'''
Table: pl_word
Description: Polish head words

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
id_bg_word 	int(11)	No		Foreign key to “bg_word”
pl_word 	varchar(100)	Yes	NULL	Polish head word
sense_index 	int(2)	No		Index of the sense
alternative_sense_index 	int(2)	No		Index of the alternative sense
latin_translation 	varchar(255)	Yes	NULL	Latin translation of the word
id_explanation 	int(11)	Yes	NULL	Foreign key to “explanation”

'''


class PlWord:

    def __init__(self):
        self.__id = None
        self.__id_bg_word = None
        self.__pl_word = None
        self.__sense_index = None
        self.__alternative_sense_index = None
        self.__latin_translation = None
        self.__id_explanation = None

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
    def id_bg_word(self):
        return self.__id_bg_word

    @id_bg_word.setter
    def id_bg_word(self, value):
        if self.__id_bg_word is None:
            self.__id_bg_word = value
        else:
            raise Exception('Already has value')

    @property
    def pl_word(self):
        return self.__pl_word

    @pl_word.setter
    def pl_word(self, value):
        if self.__pl_word is None:
            self.__pl_word = value
        else:
            raise Exception('Already has value')

    @property
    def sense_index(self):
        return self.__sense_index

    @sense_index.setter
    def sense_index(self, value):
        if self.__sense_index is None:
            self.__sense_index = value
        else:
            raise Exception('Already has value')

    @property
    def alternative_sense_index(self):
        return self.__alternative_sense_index

    @alternative_sense_index.setter
    def alternative_sense_index(self, value):
        if self.__alternative_sense_index is None:
            self.__alternative_sense_index = value
        else:
            raise Exception('Already has value')

    @property
    def latin_translation(self):
        return self.__latin_translation

    @latin_translation.setter
    def latin_translation(self, value):
        if self.__latin_translation is None:
            self.__latin_translation = value
        else:
            raise Exception('Already has value')

    @property
    def id_explanation(self):
        return self.__id_explanation

    @id_explanation.setter
    def id_explanation(self, value):
        if self.__id_explanation is None:
            self.__id_explanation = value
        else:
            raise Exception('Already has value')
