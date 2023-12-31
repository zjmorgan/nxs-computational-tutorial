# nxs-computational-tutorial

`conda env create --file environment.yml`



## Agenda 
 

### Prerequisites (MG: write guide for windows and mac) 
 * Install anaconda 
 * Install git 
 * Download repo for tutorial (inc. data and notebook) 
 * Activate conda env  
 * Install matplotlib, sciPy, lmfit, h5py 

### Intro presentation (powerpoint) 30-45 mins. 
 * What is scientific software (MG) 
 * Version control: Git and GitHub (MG) 
 * Environment management (python env and conda, pip) (JB): 
 * Running python options: scripts, python interpreter, IDE, jupyter (JB) 
 * Intro to file systems at ORNL. Where are my neutron data stored? Oncat (AS) 

### Tutorial  

#### Jean tutorial
 
 * Open notebook, Explanation of notebook (shift enter, shift enter...) 
 * Cell: imports:  
 * Exercise 1: Import data from ascii to numpy array. Do this multiple ways. Mention pandas. 
 * Exercise 2: Plot with matplotlib. Make it interactive. Show errors? 
 * Exercise 3: Extend script to for loop over multiple files 
 * Exercise 4: Create widget to do Exercise 3.  

BREAK (AS) 

#### Zach Tutorial 2 

 * Exercise 4 (SciPy): Set up fit to a peak: initial conditions, define to fit, define residual, define fit range, interpret errors (variance-covariance matrix) 
 * Exercise 5: Use LMFIT for same process.  
 * Advanced Exercise 1: Event data: Inspect nxs file with HDFView, 
 * Load neutron data and log metadata from nxs file with h5py. 
 * Advanced Ex 2: histogram events (with log binning) 
 * Super Advanced Ex 3: Re-use fitting script, fit peaks, plot position versus experimental log.   

