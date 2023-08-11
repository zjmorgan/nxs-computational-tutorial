#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

import scipy.optimize
import lmfit
import h5py

# --- load data ---

f = h5py.File('../data/elastic.nxs', mode='r')

ws = f['mantid_workspace_1/workspace/']
d_spacing_bin_edges = ws['axis1'][()]

counts  = ws['values'][()].flatten()
errors  = ws['errors'][()].flatten()

f.close()

# ---

# --- plot data ---

d_spacing = 0.5*(d_spacing_bin_edges[1:]+d_spacing_bin_edges[:-1])

#np.savetxt('../data/elastic.csv', np.column_stack([d_spacing,counts,errors]), delimiter=',')

fig, ax = plt.subplots(1,1)
ax.errorbar(d_spacing, counts, yerr=errors, fmt='.', label='data')
ax.legend(shadow=True)
ax.minorticks_on()

# ---

# --- define model ---

def model(d, A, mu, sigma, B, c):

    return A*np.exp(-0.5*(d-mu)**2/sigma**2)+B+c*d

A, mu, sigma, B, c = 800, 16, 0.3, 100, 0

p0 = (A, mu, sigma, B, c)

ax.plot(d_spacing, model(d_spacing, *p0), label='guess')
ax.legend(shadow=True)

# ---

# --- fit model ---

popt, pcov = scipy.optimize.curve_fit(model, d_spacing, counts, p0=p0,
                                      sigma=errors, absolute_sigma=True,
                                      method='lm')

ax.plot(d_spacing, model(d_spacing, *popt), label='fit')
ax.legend(shadow=True)

# ---

# --- plot residuals ---

def residual(d, counts, A, mu, sigma, B, c):
    
    return counts-model(d, A, mu, sigma, B, c)

ax.plot(d_spacing, residual(d_spacing, counts, *popt), label='residual')
ax.legend(shadow=True)

# --- 

# --- calculate errors ---

perr = np.sqrt(np.diag(pcov))

print('Fitted uncertanties as 1-std using curve_fit')
print('A     = {:8.3f} ± {:5.3f}'.format(popt[0],perr[0]))
print('mu    = {:8.3f} ± {:5.3f}'.format(popt[1],perr[1]))
print('sigma = {:8.3f} ± {:5.3f}'.format(popt[2],perr[2]))
print('B     = {:8.3f} ± {:5.3f}'.format(popt[3],perr[3]))
print('c     = {:8.3f} ± {:5.3f}'.format(popt[4],perr[4]))

# --- define weighted least squares problem ---

def weighted_deviations(x, d, counts, errors):

    A, mu, sigma, B, c = x

    return residual(d, counts, A, mu, sigma, B, c)/errors

sol = scipy.optimize.least_squares(weighted_deviations, x0=p0,
                                   args=(d_spacing, counts, errors),
                                   method='lm')

vals = sol.x

J = sol.jac
cov = np.linalg.inv(J.T.dot(J))

err = np.sqrt(np.diag(cov))

print('Fitted uncertanties as 1-std using least_squares')
print('A     = {:8.3f} ± {:5.3f}'.format(vals[0],err[0]))
print('mu    = {:8.3f} ± {:5.3f}'.format(vals[1],err[1]))
print('sigma = {:8.3f} ± {:5.3f}'.format(vals[2],err[2]))
print('B     = {:8.3f} ± {:5.3f}'.format(vals[3],err[3]))
print('c     = {:8.3f} ± {:5.3f}'.format(vals[4],err[4]))

chi2dof = np.sum(sol.fun**2)/(sol.fun.size-sol.x.size)
cov *= chi2dof

stderr = np.sqrt(np.diag(cov))

print('Fitted uncertanties as 1-stderr using least_squares')
print('A     = {:8.3f} ± {:5.3f}'.format(vals[0],stderr[0]))
print('mu    = {:8.3f} ± {:5.3f}'.format(vals[1],stderr[1]))
print('sigma = {:8.3f} ± {:5.3f}'.format(vals[2],stderr[2]))
print('B     = {:8.3f} ± {:5.3f}'.format(vals[3],stderr[3]))
print('c     = {:8.3f} ± {:5.3f}'.format(vals[4],stderr[4]))

# ---

# --- use constrained optimization ---

def weighted_residual(params, d, counts, errors):

    A = params['A']
    mu = params['mu']
    sigma = params['sigma']
    B = params['B']
    c = params['c']

    return residual(d, counts, A, mu, sigma, B, c)/errors

params = lmfit.Parameters()
params.add('A', value=A, min=0, max=np.inf)
params.add('mu', value=mu, min=-np.inf, max=np.inf)
params.add('sigma', value=sigma, min=0, max=np.inf)
params.add('B', value=B, min=0, max=np.inf)
params.add('c', value=c, min=-np.inf, max=np.inf)

result = lmfit.minimize(weighted_residual, params,
                        args=(d_spacing, counts, errors))

print('Fitted uncertanties as 1-stderr using lmfit')
for key in params.keys():
    value, stderr = result.params[key].value, result.params[key].stderr
    print('{:7} = {:8.3f} ± {:5.3f}'.format(key,value,stderr))

