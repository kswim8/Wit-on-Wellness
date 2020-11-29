# CITATION: https://towardsdatascience.com/implementing-naive-bayes-algorithm-from-scratch-python-c6880cfc9c41

def calc_statistics(self, features, target):
    '''
    calculate mean, variance for each column and convert to numpy array
    ''' 
    self.mean = features.groupby(target).apply(np.mean).to_numpy()
    self.var = features.groupby(target).apply(np.var).to_numpy()
            
    return self.mean, self.var

def gaussian_density(self, class_idx, x):     
    '''
    calculate probability from gaussian density function (normally distributed)

    '''
    mean = self.mean[class_idx]
    var = self.var[class_idx]
    numerator = np.exp((-1/2)*((x-mean)**2) / (2 * var))
    denominator = np.sqrt(2 * np.pi * var)
    prob = numerator / denominator
    return prob

# prior probabilities
def calc_prior(self, features, target):
    self.prior = (features.groupby(target).apply(lambda x: len(x))/self.rows).to_numpy()
    return self.prior
    
# posterior probabilities
def calc_posterior(self, x):
    posteriors = []
    for i in range(self.count):
        prior = np.log(self.prior[i]) 
        conditional = np.sum(np.log(self.gaussian_density(i, x)))
        posterior = prior + conditional
        posteriors.append(posterior)
    return self.classes[np.argmax(posteriors)]


def fit(self, features, target):
    # define class variables 
    self.classes = np.unique(target)
    self.count = len(self.classes)
    self.feature_nums = features.shape[1]
    self.rows = features.shape[0]
    
    # calculate statistics    
    self.calc_statistics(features, target)
    self.calc_prior(features, target)
        
def predict(self, features):
    preds = [self.calc_posterior(f) for f in features.to_numpy()]
    return preds


