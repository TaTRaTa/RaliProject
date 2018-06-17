'''
Table: explanation
Description: Explanations of the head words, derivations, phrases and examples

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
explanation 	varchar(255)	No		Explanation

'''


class Explanation:

    def __init__(self):
        self.__id = None
        self.__explanation = None

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
    def explanation(self):
        return self.__explanation

    @explanation.setter
    def explanation(self, value):
        if self.__explanation is None:
            self.__explanation = value
        else:
            raise Exception('Already has value')
