import pandas as pd
import numpy as np
#from scipy.special import alpha
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path = "../../data/drop-jump/all_participant_data_rsi.csv"
#data = np.loadtxt(path, delimiter=',', skiprows=1)
df = pd.read_csv(path)
"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

FPdata = df['force_plate_rsi'].to_numpy()
acceldata = df['accelerometer_rsi'].to_numpy()

plt.hist(FPdata, bins = 'auto', label = 'Force Plate RSI data')
plt.xlabel('Relative Force Plate RSI')
plt.ylabel('Counts')
plt.title('Force Plate Data Histogram')
plt.show()
(FP_fitted_mean, FP_fitted_std) = norm.fit(FPdata)
plt.title('Distribution of Force Plate RSI' + 'with mu =' + str(FP_fitted_mean) + 'and std =' + str(FP_fitted_std))
print('Force Plate RSI' + ' has mu =' + str(FP_fitted_mean) + 'and std =' + str(FP_fitted_std))
x = np.linspace(start = -0.25, stop = 1.5, num = 10000)
y = norm.pdf(x, loc=FP_fitted_mean, scale=FP_fitted_std)
plt.plot(x,y,label = 'normal')
plt.legend()
plt.show()

plt.hist(acceldata, bins = 15, label = 'Accelerometer RSI data')
plt.xlabel('Accelerometer Plate RSI')
plt.ylabel('Counts')
plt.title('Accelerometer Data Histogram')
plt.show()
(acl_fitted_mean, acl_fitted_std) = norm.fit(acceldata)
plt.title('Distribution of Accelerometer RSI' + 'with mu =' + str(acl_fitted_mean) + 'and std =' + str(acl_fitted_std))
print('Accelerometer RSI' + ' has mu =' + str(acl_fitted_mean) + 'and std =' + str(acl_fitted_std))
x = np.linspace( start = -0.25, stop = 1.5, num = 10000)
y = norm.pdf(x, loc=acl_fitted_mean, scale= acl_fitted_std)
plt.plot(x,y,label = 'normal')
plt.legend()
plt.show()


"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""


bins = np.linspace(0, 2, 9)
bins = np.r_[-np.inf, bins, np.inf]
expected_mu = 0
expected_std = 1
observed_counts, observed_edges = np.histogram(acceldata, bins=bins, density=False)

"""UNSURE OF HOW TO DO EXPECTED ON THIS"""
thing = norm.cdf(bins, loc=expected_mu, scale=expected_std)
expected_prob = np.diff(thing)
expected_counts = expected_prob * len(acceldata)
"""UNSURE OF HOW TO DO EXPECTED ON THIS"""

(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)
a = 0.05
if p_value < a:
    print('Reject null hypothesis. bad fit.')
else:
    print('Accept null hypothesis. good fit')


"""
Force Plate
"""
bins = np.linspace(0, 2, 9)
bins = np.r_[-np.inf, bins, np.inf]
expected_mu = 0
expected_std = 1
observed_counts, observed_edges = np.histogram(FPdata, bins=bins, density=False)

"""UNSURE OF HOW TO DO EXPECTED ON THIS"""
thing = norm.cdf(bins, loc=expected_mu, scale=expected_std)
expected_prob = np.diff(thing)
expected_counts = expected_prob * len(FPdata)
"""UNSURE OF HOW TO DO EXPECTED ON THIS"""

(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)
a = 0.05
if p_value < a:
    print('Reject null hypothesis. bad fit.')
else:
    print('Accept null hypothesis. good fit')

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')
A = 0.05
(stat, p_value) = ttest_ind(FPdata,acceldata,alternative='two-sided')
### see hypothesis-test file

'''CHECK IF IF STATEMENT IS CORRECT'''
'''
DO THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Comments are effectively used to convey the approach and describe operations conducted.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''


if p_value < A:
    print('Reject H0: RSI means for the acceleration and force plate data are NOT equivalent')
else:
    print('RSI means for the acceleration and force plate data are equivalent')

"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""


'''ADD AXIS TITIELS'''

RSIerror = abs(acceldata- FPdata)
(Er_fitted_mean, Er_fitted_std) = norm.fit(RSIerror)
plt.hist(RSIerror,bins = 16, label = 'RSI error data', density=True)
x = np.linspace(start = -1, stop = 1, num = 10000)
y = norm.pdf(x, loc = Er_fitted_mean, scale = Er_fitted_std)
plt.plot(x,y,label = 'normal')
plt.title("RSI error")
plt.legend()
plt.show()

pass
