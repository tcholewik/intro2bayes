import unittest
from src.calculator import SimpleBayes, MixtureBayes
from scipy.stats import norm

class TestBayes(unittest.TestCase):
    pass

class TestSimpleBayesWithourPriors(TestBayes):
    def setUp(self):
       self.calc = SimpleBayes()

       self.calc.add_hypothesis('Bowl1',{'Vanilla' : 0.25, 'Chocolate': 0.75}) 
       self.calc.add_hypothesis('Bowl2',{'Vanilla' : 0.5, 'Chocolate': 0.5}) 

    def test_it_gives_likelyhoods(self):

       self.assertEqual(self.calc.get_likelyhood('Vanilla','Bowl1'),0.25)
       self.assertEqual(self.calc.get_likelyhood('Vanilla','Bowl2'),0.5)
       self.assertEqual(self.calc.get_likelyhood('Chocolate','Bowl1'),0.75)
       self.assertEqual(self.calc.get_likelyhood('Chocolate','Bowl2'),0.5)

    def test_it_gives_equal_priors_if_none_were_provided(self):
       self.assertEqual(self.calc.get_prior('Bowl1'),0.5)

    def test_it_calcualates_marginal_probability(self):
       self.assertEqual(self.calc.get_marginal_probability('Vanilla'),0.375)
       self.assertEqual(self.calc.get_marginal_probability('Chocolate'),0.625)

    def test_it_calculates_posterior(self):
       self.assertAlmostEqual(self.calc.get_posterior('Bowl1','Vanilla'),0.33,1)
       self.assertAlmostEqual(self.calc.get_posterior('Bowl2','Vanilla'),0.66,1)

    def test_it_updates_probabilities(self):
       self.calc.update('Vanilla')

       self.assertAlmostEqual(self.calc.get_prior('Bowl1'),0.33,1)
       self.assertAlmostEqual(self.calc.get_prior('Bowl2'),0.66,1)

class TestSimpleBayesWithPriors(TestBayes):
    def setUp(self):
       self.calc = SimpleBayes()

       self.calc.add_hypothesis('Bowl1',{'Vanilla' : 0.25, 'Chocolate': 0.75},0.6) 
       self.calc.add_hypothesis('Bowl2',{'Vanilla' : 0.5, 'Chocolate': 0.5},0.4) 

    def test_it_can_incoporate_priors(self):
       self.assertEqual(self.calc.get_prior('Bowl1'),0.6)
       self.assertEqual(self.calc.get_prior('Bowl2'),0.4)

    def test_it_calcualates_marginal_probability(self):
       self.assertAlmostEqual(self.calc.get_marginal_probability('Vanilla'),0.35,2)
       self.assertAlmostEqual(self.calc.get_marginal_probability('Chocolate'),0.65,2)

    def test_it_calculates_posterior(self):
       self.assertAlmostEqual(self.calc.get_posterior('Bowl1','Vanilla'),0.428,2)
       self.assertAlmostEqual(self.calc.get_posterior('Bowl2','Vanilla'),0.571,2)

class TestMixtureBayes(TestBayes):
    def setUp(self):
        self.calc = MixtureBayes()

        normal1 = norm(12,3)
        normal2 = norm(12,1)
        self.calc.add_hypothesis("High Variance",normal1)
        self.calc.add_hypothesis("Low Variance",normal2)

    def test_it_gives_likelyhoods(self):
        self.assertAlmostEqual(self.calc.get_likelyhood(15,"High Variance"),0.84,2)
        self.assertAlmostEqual(self.calc.get_likelyhood(15,"Low Variance"),0.99,1)

    def test_it_calcualtes_marginal_probability(self):
        self.assertAlmostEqual(self.calc.get_marginal_probability(15),0.915,2)
        
