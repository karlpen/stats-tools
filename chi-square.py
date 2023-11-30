# Import the necessary libraries
import numpy as np
from scipy.stats import chisquare

# Create two arrays representing the observed frequencies of the rates for each period
observed_period1 = [4.716981132, 4.87804878, 3.4, 6.8, 0, 4.6, 4.3, 3.9, 4.8, 9.4]  # Replace [...] with your observed frequencies for period 1
observed_period2 = [0, 9.8, 0, 0, 0, 0, 2.958579882, 0, 0, 3.484320557]  # Replace [...] with your observed frequencies for period 2

# Perform the chi-square test
chi2_stat, p_val = chisquare(observed_period1, observed_period2)

# Output the results
print("Chi-square Statistic:", chi2_stat)
print("P-Value:", p_val)
