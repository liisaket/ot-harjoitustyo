import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luotu_kassapaate_tiedot_oikein(self):
        rahamaara = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahamaara, 100000)

        myyty_edulliset = self.kassapaate.edulliset
        self.assertEqual(myyty_edulliset, 0)

        myyty_maukkaat = self.kassapaate.maukkaat
        self.assertEqual(myyty_maukkaat, 0)
    
    def test_kateisosto_onnistuu_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_epaonnistuu_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_onnistuu_edullinen(self):
        kortti = Maksukortti(1000)
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_epaonnistuu_edullinen(self):
        kortti = Maksukortti(200)
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_onnistuu_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_epaonnistuu_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_onnistuu_maukas(self):
        kortti = Maksukortti(1000)
        onnistuiko = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_korttiosto_epaonnistuu_maukas(self):
        kortti = Maksukortti(200)
        onnistuiko = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortin_lataaminen_onnistuu(self):
        kortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(kortti, 800)
        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)
    
    def test_kortin_lataaminen_epaonnistuu(self):
        kortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
