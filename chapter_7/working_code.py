#pylint: disable-all
from math import log, sqrt, exp, pi

def CND(x):
    a1,a2,a3,a4,a5 = 0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429
    L = abs(x)

    K=1.0/(1.0+0.2316419*L)

    w=1.0-1.0/sqrt(2*pi)*exp(-L*L/2.)*(a1*K+a2*K*K+a3*pow(K,3)+a4*pow(K,4)+a5*pow(K,5))

    if x<0:
        w = 1.0-w
    return w
    

def bs_call(S, K, T, r, sigma):
    d1 = (log(S/K)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    return S*CND(d1)-K*exp(-r*T)*CND(d2)
