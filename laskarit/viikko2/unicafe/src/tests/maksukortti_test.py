import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    # Vk2 Teht. 6
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    
    def test_rahan_ottaminen_toimii(self):
        x = self.maksukortti.ota_rahaa(500)
        self.assertTrue(x, "Kortilla on rahaa 5.00 euroa")
        
        y = self.maksukortti.ota_rahaa(600)
        self.assertFalse(y, "Kortilla on rahaa 5.00 euroa")
