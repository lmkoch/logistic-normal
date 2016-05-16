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

    :param data:    array, shape (D,N)
                    D: number of categories (dimensions),
                    N: number of samples
    :return: mu and cov: parameters of the logistic normal distribution
    """

    # TODO: input validation

    # transform the data with the logit function
    # y = [log(x1/xD), ..., log(x_{D-1}/xD)]

    # divide all values by last row and apply log
    y = np.log(data[:-1,:] / data[-1,:])

    # calculate the mean and covariance of transformed data
    mu = np.average(y, axis=1)
    covar = np.cov(y)

    return mu, covar


def pdf(mu, covar):
    """
    Returns a D-dimensional logistic-normal PDF function

    :param mu: array, shape (D-1,)
    :param covar: array, shape (D-1,D-1)
    :return: logisticnormal function handle
    """

    D = mu.shape[0] + 1

    if covar.shape != (D-1,D-1):
        raise Exception('Parameter dimension mismatch. mu.shape is {}, covar.shape is {}'.format(mu.shape, covar.shape))

    def logisticnormal(x):
        """
        :param x:   array, shape (D,N)
                    D: number of categories (dimensions),
                    N: number of samples
        :return: f(x)
        """

        if x.shape[0] != D:
            raise Exception('Data dimension mismatch. Number of rows should be {}, but is {}'.format(D, x.shape[0]))

        y = np.log(x[:-1,:] / x[-1,:]).T

        # apply multivariate normal pdf
        return multivariate_normal.pdf(y, mean=mu, cov=covar, allow_singular=True)

    return logisticnormal

