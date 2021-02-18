# extracting the address is the most important part
# and therefore I picked 22 random addresses from google maps and tested the function with it
# just to make sure the function catch the most addresses "its not possible to catch all possible addresses just with regex"
import unittest
import image_processing
# defining test cases
test1="Am Tag der deutschen Einheit haben wir eine Party am 13.11.2021 um 18:00 uhr , Die Adresse : An der Bicke 9, 34508 Willingen "
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
        self.assertEqual(a,"An der Bicke 9, 34508 Willingen")
    def test_get_adress2(self):
        a=image_processing.get_address(test2)
        self.assertEqual(a,"Lützenkirchener Str. 271, 51381 Leverkusen")
    def test_get_adress3(self):
        a = image_processing.get_address(test3)
        self.assertEqual(a, "Prenzlauer Allee 231, 10405 Berlin")
    def test_get_adress4(self):
        a=image_processing.get_address(test4)
        self.assertEqual(a,"Dorfstraße 61A, 18249 Warnow")
    def test_get_adress5(self):
        a=image_processing.get_address(test5)
        self.assertEqual(a,"Königsberger Pl. 21A, 51371 Leverkusen")
    def test_get_adress6(self):
        a=image_processing.get_address(test6)
        self.assertEqual(a,"Daimlerstraße 38 , 22763 Hamburg")
    def test_get_adress7(self):
        a=image_processing.get_address(test7)
        self.assertEqual(a,"Fröbelstraße 17, 10405 Berlin")
    def test_get_adress8(self):
        a=image_processing.get_address(test8)
        self.assertEqual(a,"Fröbelweg 3, 66352 Großrosseln")
    def test_get_adress9(self):
        a=image_processing.get_address(test9)
        self.assertEqual(a,"Ernst-Thälmann-Ring 11, 17491 Greifswald")
    def test_get_adress10(self):
        a=image_processing.get_address(test10)
        self.assertEqual(a,"Ernst-Thälmann-Platz 4, 17498 Neuenkirchen")
    def test_get_adress11(self):
        a=image_processing.get_address(test11)
        self.assertEqual(a,"Am Ortfelde 25, 30916 Isernhagen")
    def test_get_adress12(self):
        a=image_processing.get_address(test12)
        self.assertEqual(a,"Westendorf 19, 38372 Büddenstedt")
    def test_get_adress13(self):
        a=image_processing.get_address(test13)
        self.assertEqual(a,"Schäferbreite 4, 38364 Schöningen")
    def test_get_adress14(self):
        a=image_processing.get_address(test14)
        self.assertEqual(a,"Volkwardingen 22, 29646 Bispingen")
    def test_get_adress15(self):
        a=image_processing.get_address(test15)
        self.assertEqual(a,"Heidkamp 1, 29646 Bispingen")
    def test_get_adress16(self):
        a=image_processing.get_address(test16)
        self.assertEqual(a,"Heberer Str. 10, 29646 Bispingen")
    def test_get_adress17(self):
        a=image_processing.get_address(test17)
        self.assertEqual(a,"Holstentorplatz 7, 23552 Lübeck")
    def test_get_adress18(self):
        a=image_processing.get_address(test18)
        self.assertEqual(a,"Binnenland 30, 23556 Lübeck")
    def test_get_adress19(self):
        a=image_processing.get_address(test19)
        self.assertEqual(a,"Melkerstieg 1, 23556 Lübeck")
    def test_get_adress20(self):
        a=image_processing.get_address(test20)
        self.assertEqual(a,"Drögeneck 68, 23556 Lübeck")
    def test_get_adress21(self):
        a=image_processing.get_address(test21)
        self.assertEqual(a,"Moorweg 14, 23795 Groß Rönnau")
    def test_get_adress22(self):
        a=image_processing.get_address(test22)
        self.assertEqual(a,"Stüff 2, 23795 Negernbötel")

if __name__ == '__main__':
    unittest.main()
