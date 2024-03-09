#pylint: disable-all
from scipy import stats
from numpy import log,exp,sqrt
    
def bs_call(S, K, T, r, sigma):
    d1 = (log(S/K)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    return S*stats.norm.cdf(d1)-K*exp(-r*T)*stats.norm.cdf(d2)
