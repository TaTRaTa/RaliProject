class Factory:
    def __init__(self
                 , root
                 , BgWord
                 , BgWordExample
                 , Characheristic
                 , CharacteristicType
                 , Explanation
                 , MissingWord
                 , MmBgWordCharacteristic
                 , MmBgWordExampleCharacteristic
                 , MmExplanationCharacteristic
                 , MmPlWordCharacteristic
                 , PlWord
                 , PlWordExample):
        self.__root = root
        self.__bg_word = BgWord()
        self.__bg_word_example = BgWordExample()
        self.__characteritic = Characheristic()
        self.__characteristic_type = CharacteristicType()
        self.__explanation = Explanation()
        self.__missing_word = MissingWord()
        self.__mm_bg_word_characteristic = MmBgWordCharacteristic()
        self.__mm_bg_word_example_characteristic = MmBgWordExampleCharacteristic()
        self.__mm_explanation_characteristic = MmExplanationCharacteristic()
        self.__mm_pl_word_characteristic = MmPlWordCharacteristic()
        self.__pl_word = PlWord()
        self.__pl_word_example = PlWordExample()

    def run(self):
        for child in self.__root:
            print(child)

            if child.tag == 'hw':
                print('-', child.text)
                self.__bg_word.bg_word = child.text
                if str(child.text).find('|') != -1:
                    self.__bg_word.suffix = child.text[child.text.find('|') + 1:]
            elif child.tag == 'alt':
                for t in child:
                    print('--', t.tag, t.text)
            elif child.tag == 'gen':
                print('-', child.text)
            elif child.tag == 'struc':
                print('-', child.attrib)
                for t in child:
                    print('--', t.tag)
                    if t.tag == 'alt':
                        for a in t:
                            print('---', a.tag, a.text)
            elif child.tag == 'eg':
                for t in child:
                    if t.tag == 'usd':
                        print('--', t.attrib)
                    print('--', t.tag, t.text)
            elif child.tag == 'pos':
                print('-', t.text)
            elif child.tag == 'gram':
                print('-', t.text)
            elif child.tag == 'subc':
                print('-', t.text)
            elif child.tag == 'conjugation':
                for t in child:
                    print('--', t.tag, t.text)
            elif child.tag == 'usg':
                print(child.attrib)
                print('-', t.text)
            elif child.tag == 'xr':
                print('-', t.text)

    def test(self):
        for child in self.__root:
            print(child)

            if child.tag == 'hw':
                print('-', child.text)
            elif child.tag == 'alt':
                for t in child:
                    print('--', t.tag, t.text)
            elif child.tag == 'gen':
                print('-', child.text)
            elif child.tag == 'struc':
                print('-', child.attrib)
                for t in child:
                    print('--', t.tag)
                    if t.tag == 'alt':
                        for a in t:
                            print('---', a.tag, a.text)
            elif child.tag == 'eg':
                for t in child:
                    if t.tag == 'usd':
                        print('--', t.attrib)
                    print('--', t.tag, t.text)
            elif child.tag == 'pos':
                print('-', t.text)
            elif child.tag == 'gram':
                print('-', t.text)
            elif child.tag == 'subc':
                print('-', t.text)
            elif child.tag == 'conjugation':
                for t in child:
                    print('--', t.tag, t.text)
            elif child.tag == 'usg':
                print(child.attrib)
                print('-', t.text)
            elif child.tag == 'xr':
                print('-', t.text)

    def test_bg_word(self):
        print(self.__bg_word.bg_word)
        print(self.__bg_word.suffix)