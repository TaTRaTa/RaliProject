'''
Table: bg_word
Description: Bulgarian head words

Field	Type	Null	Default	Comments
id 	int(11)	No		Id
homonym_index 	int(1)	Yes	NULL	Index of the homonym (if null, no homonym exists)
bg_word 	varchar(100)	No		Bulgarian head word
suffix 	varchar(20)	Yes	NULL	Suffix
plural	varchar(20)	Yes	NULL	Plural form for a noun
is_plural_rare 	int(1)	Yes	NULL	Frequency of usage of the plural form for a noun (null – normal, 0 - often, 1 – rare)
conjugation 	varchar(20)	Yes	NULL	Conjugation form for a verb (2 p., present)
conjugation_type 	int(1)	Yes	NULL	Type of conjugation for a verb (1, 2 or 3)
has_gender 	int(1)	Yes	NULL	Whether a noun has feminine and neuter gender
gender_feminine 	varchar(20)	Yes	NULL	Feminine gender form for an adjective
gender_neuter 	varchar(20)	Yes	NULL	Neuter gender form for an adjective
id_explanation 	int(11)	Yes	NULL	Foreign key to “explanation”
id_bg_word 	int(11)	Yes	NULL	Id of the referent Bulgarian word
referent_bg_word 	varchar(255)	Yes	NULL	Referent Bulgarian word

'''


class BgWord:

    def __init__(self):
        self.__id = None
        self.__homonym_index = None
        self.__bg_word = None
        self.__suffix = None
        self.__plural = None
        self.__is_plural_rare = None
        self.__conjugation = None
        self.__conjugation_type = None
        self.__has_gender = None
        self.__gender_feminine = None
        self.__genter_neuter = None
        self.__id_explanation = None
        self.__id_bg_word = None
        self.__referent_bg_word = None

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
    def homonym_index(self):
        return self.__homonym_index

    @homonym_index.setter
    def homonym_index(self, value):
        if self.__homonym_index is None:
            self.__homonym_index = value
        else:
            raise Exception('Already has value')

    @property
    def bg_word(self):
        return self.__bg_word

    @bg_word.setter
    def bg_word(self, value):
        if self.__bg_word is None:
            self.__bg_word = value
        else:
            raise Exception('Already has value')

    @property
    def suffix(self):
        return self.__suffix

    @suffix.setter
    def suffix(self, value):
        if self.__suffix is None:
            self.__suffix = value
        else:
            raise Exception('Already has value')

    @property
    def plural(self):
        return self.__plural

    @plural.setter
    def plural(self, value):
        if self.__plural is None:
            self.__plural = value
        else:
            raise Exception('Already has value')

    @property
    def is_plural_rare(self):
        return self.__is_plural_rare

    @is_plural_rare.setter
    def is_plural_rare(self, value):
        if self.__is_plural_rare is None:
            self.__is_plural_rare = value
        else:
            raise Exception('Already has value')

    @property
    def conjugation(self):
        return self.__conjugation

    @conjugation.setter
    def conjugation(self, value):
        if self.__conjugation is None:
            self.__conjugation = value
        else:
            raise Exception('Already has value')

    @property
    def conjugation_type(self):
        return self.__conjugation_type

    @conjugation_type.setter
    def conjugation_type(self, value):
        if self.__conjugation_type is None:
            self.__conjugation_type = value
        else:
            raise Exception('Already has value')

    @property
    def has_gender(self):
        return self.__has_gender

    @has_gender.setter
    def has_gender(self, value):
        if self.__has_gender is None:
            self.__has_gender = value
        else:
            raise Exception('Already has value')

    @property
    def gender_feminine(self):
        return self.__gender_feminine

    @gender_feminine.setter
    def gender_feminine(self, value):
        if self.__gender_feminine is None:
            self.__gender_feminine = value
        else:
            raise Exception('Already has value')

    @property
    def genter_neuter(self):
        return self.__genter_neuter

    @genter_neuter.setter
    def genter_neuter(self, value):
        if self.__genter_neuter is None:
            self.__genter_neuter = value
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
    def referent_bg_word(self):
        return self.__referent_bg_word

    @referent_bg_word.setter
    def referent_bg_word(self, value):
        if self.__referent_bg_word is None:
            self.__referent_bg_word = value
        else:
            raise Exception('Already has value')



