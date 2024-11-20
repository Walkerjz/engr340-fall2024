import pandas as pd
import numpy as np
#from scipy.special import alpha
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path = "../../data/drop-jump/all_participant_data_rsi.csv"
#put the data in a data frame
df = pd.read_csv(path)
"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')
#put the Force Plate and accelerometer RSI values in different arrays
FPdata = df['force_plate_rsi'].to_numpy()
acceldata = df['accelerometer_rsi'].to_numpy()

#make a histogram plot of the Force plate data
plt.hist(FPdata, bins = 'auto', label = 'Force Plate RSI data')
plt.xlabel('Relative Force Plate RSI')
plt.ylabel('Counts')
plt.title('Force Plate Data Histogram')
plt.show()

#calculate statistics to fit a normal to the force plate RSI data
(FP_fitted_mean, FP_fitted_std) = norm.fit(FPdata)

#generate title for normal and add and also print the calculated statistics
plt.title('Distribution of Force Plate RSI' + 'with mu =' + str(FP_fitted_mean) + 'and std =' + str(FP_fitted_std))
print('Force Plate RSI' + ' has mu =' + str(FP_fitted_mean) + 'and std =' + str(FP_fitted_std))

#generate the actual normal curve with x and y
x = np.linspace(start = -0.25, stop = 1.5, num = 10000)
y = norm.pdf(x, loc=FP_fitted_mean, scale=FP_fitted_std)

#plot it all
plt.plot(x,y,label = 'normal')
plt.legend()
plt.show()

#make a histogram plot of the accelerometer data
plt.hist(acceldata, bins = 15, label = 'Accelerometer RSI data')
plt.xlabel('Accelerometer Plate RSI')
plt.ylabel('Counts')
plt.title('Accelerometer Data Histogram')
plt.show()

#calculate statistics to fit a normal to the accelerometer RSI data
(acl_fitted_mean, acl_fitted_std) = norm.fit(acceldata)

#generate title for normal and add and also print the calculated statistics
plt.title('Distribution of Accelerometer RSI' + 'with mu =' + str(acl_fitted_mean) + 'and std =' + str(acl_fitted_std))
print('Accelerometer RSI' + ' has mu =' + str(acl_fitted_mean) + 'and std =' + str(acl_fitted_std))

#generate the actual normal curve with x and y
x = np.linspace( start = -0.25, stop = 1.5, num = 10000)
y = norm.pdf(x, loc=acl_fitted_mean, scale= acl_fitted_std)

#plot it all
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
#generate 9 bins between [0,2)
bins = np.linspace(0, 2, 9)

#append -inf and +inf to both ends of the bins
bins = np.r_[-np.inf, bins, np.inf]

#expected statistics
expected_mu = 0
expected_std = 1

#find observed counts in each bin
observed_counts, observed_edges = np.histogram(acceldata, bins=bins, density=False)

###Find probability a sample is in a bin
expected_prob = np.diff(norm.cdf(bins, loc=expected_mu, scale=expected_std))

#multiply the probability by the number of samples to get the expected counts in each bin
expected_counts = expected_prob * len(acceldata)

#Generate and print chisquare statistics
(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

#define alpha
a = 0.05

#compare alpha to p value to determine if the null hypothesis should be chosen
if p_value < a:
    print('Reject null hypothesis. bad fit.')
else:
    print('Accept null hypothesis. good fit')

"""
Force Plate
"""
#generate 9 bins between [0,2)
bins = np.linspace(0, 2, 9)

#append -inf and +inf to both ends of the bins
bins = np.r_[-np.inf, bins, np.inf]

#expected statistics
expected_mu = 0
expected_std = 1

#find observed counts in each bin
observed_counts, observed_edges = np.histogram(FPdata, bins=bins, density=False)

###Find probability a sample is in a bin
expected_prob = np.diff(norm.cdf(bins, loc=expected_mu, scale=expected_std))
expected_counts = expected_prob * len(FPdata)

#Generate and print chisquare statistics
(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat: ', chi_stat, 'p-value: ', p_value)

#define alpha
a = 0.05

#compare alpha to p value to determine if the null hypothesis should be chosen
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
#define alpha
A = 0.05

#calculate test statistics
(stat, p_value) = ttest_ind(FPdata,acceldata,alternative='two-sided')

### print the P-value
print('the p-value is: ' + str(p_value) +' and alpha is: 0.05')

### see if the RSI values from the force plate and accelerometer are equal
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

### calculate error between force plate and accelerometer RSI values, didn't absolute value it so the data set is more symmetric
RSIerror = acceldata- FPdata

### calculate mean and std to fit a normal distribution
(Er_fitted_mean, Er_fitted_std) = norm.fit(RSIerror)

### plot a histogram, density is to show what percentage of value in a bin rather than counts to make the graph scaling better
plt.hist(RSIerror,bins = 16, label = 'RSI error data', density=True)

### calculate the x and y values of a normal curve fitted to the RSI error
x = np.linspace(start = -1, stop = 1, num = 10000)
y = norm.pdf(x, loc = Er_fitted_mean, scale = Er_fitted_std)

### plot the normal on the same graph
plt.plot(x,y,label = 'normal')
plt.title("RSI error")
plt.ylabel("Density")
plt.xlabel('RSI measurement error')
plt.legend()
plt.show()

