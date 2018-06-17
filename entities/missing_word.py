'''
Table: missing_word
Description: Registered missing words in the dictionary by the end users

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
word 	varchar(255)	No		Missing head word
bg_pl 	int(1)	No		Whether it is Bulgarian or Polish (1 - Bulgarian, 2 – Polish)
comment 	varchar(255)	Yes	NULL	Comment of the end user
served 	int(1)	Yes	NULL	Whether the word is entered in the database by un administrator  (0 - no, 1 - yes)

'''

class MissingWord:

    def __init__(self):
        self.__id = None
        self.__word = None
        self.__bg_pl = None
        self.__comment = None
        self.__served = None

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
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        if self.__word is None:
            self.__word = value
        else:
            raise Exception('Already has value')

    @property
    def bg_pl(self):
        return self.__bg_pl

    @bg_pl.setter
    def bg_pl(self, value):
        if self.__bg_pl is None:
            self.__bg_pl = value
        else:
            raise Exception('Already has value')

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        if self.__comment is None:
            self.__comment = value
        else:
            raise Exception('Already has value')

    @property
    def served(self):
        return self.__served

    @served.setter
    def served(self, value):
        if self.__served is None:
            self.__served = value
        else:
            raise Exception('Already has value')
