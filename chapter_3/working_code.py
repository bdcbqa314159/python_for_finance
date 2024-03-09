#pylint: disable-all
import math

def pv_f(fv, r=0.1, n=1):
    return fv/(1+r)**n

def perpetuity(c, r, g = 0.):
    if r<=g:
        print(f"{r}<={g}")
        return 
    return c/(r-g)

def pv_annuity(pmt, r, n):
    if not r > 0.:
        return None
    return (pmt/r)*(1 - 1/(1+r)**n)

def pv_annuity_due(pmt, r, n):
    return pv_annuity(pmt, r, n)*(1+r)

def fv_annuity(pmt, r, n):
    return pv_annuity(pmt,r,n)*(1+r)**n

def fv_annuity_due(pmt, r, n):
    return pv_annuity(pmt,r,n)*(1+r)**(n+1)


def pv_growing_annuity(pmt, r, n,g):
    if not r > 0. or g-r == 0.:
        return None
    return (pmt/(r-g))*(1 - ((1+g)/(1+r))**n)

def fv_growing_annuity(pmt, r, n, g):
    return pv_growing_annuity(pmt,r,n,g)*(1+r)**n

def ear(apr, m):
    return (1+apr/m)**m - 1

def apr(ear, m):
    return ((1+ear)**(1/m) - 1)*m

def r_eff_m(apr_m, m):
    return apr_m/m

def r_eff_m_2(apr_m_1, m_1, m_2):
    return (1+apr_m_1/m_1)**(m_1/m_2) - 1

def r_cont(apr, m):
    return m*math.log(1 + apr/m)

def npv_f(rate, cashflows):
    total = 0.
    for i, cashflow in enumerate(cashflows):
        total += cashflow/(1+rate)**i
    return total

def IRR_f(cashflows, iterations = 100):
    rate = 1.

    investment = cashflows[0]
    for i in range(1, iterations+1):
        rate *= (1-npv_f(cashflows, rate)/investment)
    return rate



