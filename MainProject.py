# -*- coding: utf-8 -*-
import os
import sys
import xml.etree.ElementTree as ET

from Factory import Factory
from entities.bg_word import BgWord
from entities.bg_word_example import BgWordExample
from entities.characteristic import Characheristic
from entities.characteristic_type import CharacteristicType
from entities.explanation import Explanation
from entities.missing_word import MissingWord
from entities.mm_bg_word_characteristic import MmBgWordCharacteristic
from entities.mm_bg_word_example_characteristic import MmBgWordExampleCharacteristic
from entities.mm_explanation_characteristic import MmExplanationCharacteristic
from entities.mm_pl_word_characteristic import MmPlWordCharacteristic
from entities.pl_word import PlWord
from entities.pl_word_example import PlWordExample


def main():

    file = os.path.join(os.getcwd(), os.path.normpath("./XMLs_examples/example1.xml"))
    # file = os.path.join(os.getcwd(), os.path.normpath("./XMLs_examples/example2.xml"))
    # file = os.path.join(os.getcwd(), os.path.normpath("./XMLs_examples/example3.xml"))
    # file = os.path.join(os.getcwd(), os.path.normpath("./XMLs_examples/example4.xml")) # wrong xml (more then 1  root)
    # file = os.path.join(os.getcwd(), os.path.normpath("./XMLs_examples/example5.xml"))

    tree = ET.parse(file)
    root = tree.getroot()

    businessLogic = Factory(root
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
                            , PlWordExample)

    # businessLogic.test()
    businessLogic.run()
    print('==================================')
    businessLogic.test_bg_word()

if __name__ == '__main__':
    main()

