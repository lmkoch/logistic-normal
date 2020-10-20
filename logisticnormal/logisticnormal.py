__author__ = 'lkoch'


import numpy as np

from scipy.stats import multivariate_normal

__all__ = [
    'pdf',
    'fit',
]


def fit(data):
    """
    Estimate parameters of logistic normal distribution by estimating the multivariate gaussian distribution of the
    logit-transformed data

    :param data:    array, shape (N,D)
                    N: number of samples,
                    D: number of categories (dimensions)
    :return: mu and cov: parameters of the logistic normal distribution
    """

    # TODO: input validation

    # transform the data with the logit function
    # y = [log(x1/xD), ..., log(x_{D-1}/xD)]

    # divide all values by last column and apply log
    y = np.log(data[:,:-1] / data[:,-1][:, None])

    # calculate the mean and covariance of transformed data
    mu = np.average(y, axis=0)
    covar = np.cov(y.T)

    return mu, covar


def pdf(mu, covar):
    """
    Returns a D-dimensional logistic-normal PDF function

    :param mu: array, shape (D-1,)
    :param covar: array, shape (D-1,D-1)
    :return: logisticnormal function handle
    """

    mu = np.atleast_1d(mu)
    covar = np.atleast_2d(covar)

    D = len(np.ravel(mu)) + 1

    if covar.shape != (D-1,D-1):
        raise Exception('Parameter dimension mismatch. mu.shape is {}, covar.shape is {}'.format(mu.shape, covar.shape))

    def logisticnormal(x):
        """ Corrected version - I suspect the version above is wrong

        :param x:   array, shape (N,D)
                    N: number of samples,
                    D: number of categories (dimensions)
        :return: f(x)
        """

        if x.shape[1] != D:
            raise Exception('Data dimension mismatch. Number of rows should be {}, but is {}'.format(D, x.shape[0]))

        y = np.log(x[:,:-1] / (x[:,-1][:, None]+0.0000001))

        # apply multivariate normal pdf
        return multivariate_normal.pdf(y, mean=mu, cov=covar, allow_singular=True) / np.prod(x, axis=1)

    return logisticnormal

