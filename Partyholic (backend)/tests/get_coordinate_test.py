# testing on 22 String to extract the address first and after that getting the coordinate from it
# if get_coordinate() could not find the coordinate for the given address , it will return None

import unittest
import image_processing
# defining test cases
test1="Am Tag der deutschen Einheit haben wir eine Party am 13.11.2021 um 18:00 uhr , Die Adresse : An der Bicke 9, 34508 Willingen"
test2="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Lützenkirchener Str. 271, 51381 Leverkusen eingeladen"
test3="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr Prenzlauer Allee 231, 10405 Berlin eingeladen. "
test4="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Dorfstraße 61A, 18249 Warnow eingeladen. "
test5="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Königsberger Pl. 21A, 51371 Leverkusen eingeladen. "
test6="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Daimlerstraße 38 , 22763 Hamburg eingeladen. "
test7="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Fröbelstraße 17, 10405 Berlin eingeladen. "
test8="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Fröbelweg 3, 66352 Großrosseln eingeladen. "
test9="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Ernst-Thälmann-Ring 11, 17491 Greifswald eingeladen. "
test10="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Ernst-Thälmann-Platz 4, 17498 Neuenkirchen eingeladen. "
test11="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Am Ortfelde 25, 30916 Isernhagen eingeladen. "
test12="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Westendorf 19, 38372 Büddenstedt eingeladen. "
test13="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Schäferbreite 4, 38364 Schöningen eingeladen. "
test14="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Volkwardingen 22, 29646 Bispingen eingeladen. "
test15="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Heidkamp 1, 29646 Bispingen eingeladen. "
test16="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Heberer Str. 10, 29646 Bispingen eingeladen. "
test17="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Holstentorplatz 7, 23552 Lübeck eingeladen. "
test18="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Binnenland 30, 23556 Lübeck eingeladen. "
test19="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Melkerstieg 1, 23556 Lübeck eingeladen. "
test20="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Drögeneck 68, 23556 Lübeck eingeladen. "
test21="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Moorweg 14, 23795 Groß Rönnau eingeladen. "
test22="Sie sind zu Das Ende der Welt Party am Donnerstag ,den 13 . Januar . 2020 um 12 uhr in Stüff 2, 23795 Negernbötel eingeladen. "

class MyTestCase(unittest.TestCase):
    def test_get_adress1(self):
        a=image_processing.get_address(test1)
        coordinate=image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress2(self):
        a=image_processing.get_address(test2)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress3(self):
        a = image_processing.get_address(test3)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress4(self):
        a=image_processing.get_address(test4)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress5(self):
        a=image_processing.get_address(test5)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress6(self):
        a=image_processing.get_address(test6)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress7(self):
        a=image_processing.get_address(test7)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress8(self):
        a=image_processing.get_address(test8)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress9(self):
        a=image_processing.get_address(test9)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress10(self):
        a=image_processing.get_address(test10)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress11(self):
        a=image_processing.get_address(test11)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress12(self):
        a=image_processing.get_address(test12)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress13(self):
        a=image_processing.get_address(test13)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress14(self):
        a=image_processing.get_address(test14)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress15(self):
        a=image_processing.get_address(test15)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress16(self):
        a=image_processing.get_address(test16)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress17(self):
        a=image_processing.get_address(test17)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress18(self):
        a=image_processing.get_address(test18)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress19(self):
        a=image_processing.get_address(test19)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress20(self):
        a=image_processing.get_address(test20)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress21(self):
        a=image_processing.get_address(test21)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)
    def test_get_adress22(self):
        a=image_processing.get_address(test22)
        coordinate = image_processing.get_coordinate(a)
        self.assertNotEqual(coordinate,None)

if __name__ == '__main__':
    unittest.main()
