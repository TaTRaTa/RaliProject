'''
Table: pl_word_example
Description: Examples of the polish head words

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
id_pl_word 	int(11)	No		Foreign key to “pl_word”
example 	varchar(255)	No		Example in Polish
id_explanation 	int(11)	Yes	NULL	Foreign key to “explanation”

'''


class PlWordExample:

    def __init__(self):
        self.__id = None
        self.__id_pl_word = None
        self.__example = None
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
    def id_pl_word(self):
        return self.__id_pl_word

    @id_pl_word.setter
    def id_pl_word(self, value):
        if self.__id_pl_word is None:
            self.__id_pl_word = value
        else:
            raise Exception('Already has value')

    @property
    def example(self):
        return self.__example

    @example.setter
    def example(self, value):
        if self.__example is None:
            self.__example = value
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
