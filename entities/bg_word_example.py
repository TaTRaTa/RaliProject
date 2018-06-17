'''
Table: bg_word_example
Description: Derivations, phrases or examples of the bulgarian head words and their translation in polish

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
id_bg_word 	int(11)	No		Foreign key to “bg_word”
before_word 	varchar(100)	Yes	NULL	Text before the head word
after_word 	varchar(100)	Yes	NULL	Text after the head word
type 	int(1)	No		Type of the usage (1 - Derivation; 2 - Phrase; 3 - Example)
pl_translation 	varchar(255)	Yes	NULL	Polish translation
id_explanation 	int(11)	Yes	NULL	Foreign key to “exlanation”

'''


class BgWordExample:

    def __init__(self):
        self.__id = None
        self.__id_bg_word = None
        self.__before_word = None
        self.__after_word = None
        self.__type = None
        self.__pl_translation = None
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
    def before_word(self):
        return self.__before_word

    @before_word.setter
    def before_word(self, value):
        if self.__before_word is None:
            self.__before_word = value
        else:
            raise Exception('Already has value')

    @property
    def after_word(self):
        return self.__after_word

    @after_word.setter
    def after_word(self, value):
        if self.__after_word is None:
            self.__after_word = value
        else:
            raise Exception('Already has value')

    @property
    def type_i(self):
        return self.__type

    @type_i.setter
    def type_i(self, value):
        if self.__type is None:
            self.__type = value
        else:
            raise Exception('Already has value')

    @property
    def pl_translation(self):
        return self.__pl_translation

    @pl_translation.setter
    def pl_translation(self, value):
        if self.__pl_translation is None:
            self.__pl_translation = value
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
