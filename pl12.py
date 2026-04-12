##Descriptive Statistics And Inferential Statistics
##Hypothesis testing ___()_____ if (Confidence Interval) aka alpha 0.05 then less than -0.025 and greater than 0.025 is rejected area for the hypothesis
##, CI = 95/97/99 even 93 in simulations
##Z= (sample mean(x bar) - population mean(meu))/stnd dev(sigma) /root of x
import math
from scipy.stats import norm
#Sample data
##data = df['A'].mean()
sample_mean = 169.5
population_mean = 168
population_std_dev = 3.9
sample_size = 36
alpha = 0.05
tail = 'right'
#Standard error
standard_error = population_std_dev / math.sqrt(sample_size)
#Z-Score
z_score = (sample_mean - population_mean) / standard_error
#p-value based on the type of data
if tail == 'two':
    p_value = 2*(1-norm.cdf(abs(z_score)))
    print(norm.cdf(abs(z_score)))
elif tail == 'left':
    p_value = norm.cdf(abs(z_score))
    print(norm.cdf(abs(z_score)))
elif tail == 'right':
    p_value = 1- norm.cdf(z_score)
    print(norm.cdf(abs(z_score)))
else:
    raise Valueerror("Tail must be 'two', 'left', or 'right'")
#output
if p_value<alpha:
    conclusion = "Reject the null hypothesis"
else:
    conclusion = "Fail to reject the null hypothesis"
print(f"Z-score:{z_score:.4f}")
print(f"P-value:{p_value:.4f}")
print(f"Conclusion: {conclusion}")
