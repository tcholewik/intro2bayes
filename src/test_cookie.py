
import unittest
from src.cookies import CookieBowl

class TestCookieBowl(unittest.TestCase):
    def test_it_accepts_likelyhoods(self):
        bowl = CookieBowl(vanilla=0.25)
        
    def test_it_produces_cookies(self):
        bowl = CookieBowl(vanilla=0.25)
        self.assertIn(bowl.draw(),['Vanilla','Chocolate'])

    def test_it_can_have_only_vanilla_cookies(self):
        bowl = CookieBowl(vanilla=1)
        for _ in range(10):
            self.assertEquals(bowl.draw(),'Vanilla')
    
    def test_it_can_have_only_chocolata_cookies(self):
        bowl = CookieBowl(vanilla=0)
        for _ in range(10):
            self.assertEquals(bowl.draw(),'Chocolate')

    def test_it_can_draw_both_cookies(self):
        bowl = CookieBowl(vanilla=0.5)
        cookies = list()
        for _ in range(20):
            cookies.append(bowl.draw())
        self.assertIn('Vanilla',cookies)
        self.assertIn('Chocolate',cookies)
