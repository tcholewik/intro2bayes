
class SimpleBayes(object):
    def __init__(self):
        self.hypothesises = dict()
        self.priors = dict()

    def add_hypothesis(self,name,likeyhood,prior = None):
        self.hypothesises[name] = likeyhood
        self.priors[name] = prior

    def get_likelyhood(self,data,hypothesis):
        likelyhoods = self.hypothesises[hypothesis]
        return likelyhoods[data]

    def get_prior(self,hypothesis):
        requested_prior = self.priors[hypothesis]
        if requested_prior is None:
            requested_prior = 1 / float(len(self.priors))
        return requested_prior

    def get_marginal_probability(self,data):
        sum_of_likelyhoods = 0
        for name in self.hypothesises.keys():
            sum_of_likelyhoods += self.get_prior(name) * self.get_likelyhood(data,name)
        return sum_of_likelyhoods
        
    def get_posterior(self,hypothesis,data):
        return \
            self.get_prior(hypothesis) * \
            self.get_likelyhood(data,hypothesis) / \
            self.get_marginal_probability(data)

    def update(self,data):
        posteriors = dict()
        for hypothesis in self.priors.keys():
            posteriors[hypothesis] = self.get_posterior(hypothesis,data)
        self.priors = posteriors

class MixtureBayes(SimpleBayes):
    def get_likelyhood(self,data,hypothesis):
        likelyhoods = self.hypothesises[hypothesis]
        return likelyhoods.cdf(data)
