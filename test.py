from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the normal distribution
mu, sigma = 0, 0.1  # mean and standard deviation

# Generate a sequence of numbers from -3*sigma to 3*sigma
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

# Plot the probability density function (PDF)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.title('Normal Distribution')
plt.show()

from scipy.stats import binom

# Define parameters for the binomial distribution
n, p = 10, 0.5  # number of trials and success probability

# Generate a range of numbers of successes
k = np.arange(0, 11)

# Calculate the probability mass function (PMF)
pmf = binom.pmf(k, n, p)

# Plot the PMF
plt.stem(k, pmf)
plt.title('Binomial Distribution')
plt.xlabel('Number of successes')
plt.ylabel('Probability')
plt.show()

from scipy.stats import poisson

# Define the parameter for the Poisson distribution
lambda_ = 3  # average rate

# Generate a range of numbers of events
k = np.arange(0, 20)

# Calculate the PMF
pmf = poisson.pmf(k, lambda_)

# Plot the PMF
plt.stem(k, pmf)
plt.title('Poisson Distribution')
plt.xlabel('Number of events')
plt.ylabel('Probability')
plt.show()


from scipy.stats import expon

# Define the scale parameter for the exponential distribution
scale = 1.0  # inverse of rate (lambda)

# Generate a sequence of numbers
x = np.linspace(0, 10, 100)

# Plot the probability density function (PDF)
plt.plot(x, expon.pdf(x, scale=scale))
plt.title('Exponential Distribution')
plt.show()

from scipy.stats import uniform

# Define the parameters for the uniform distribution
start, width = 0, 1  # start and width of the distribution

# Generate a sequence of numbers
x = np.linspace(start, start + width, 100)

# Plot the probability density function (PDF)
plt.plot(x, uniform.pdf(x, start, width))
plt.title('Uniform Distribution')
plt.show()


from scipy.stats import chi2

# Define the degrees of freedom for the chi-squared distribution
df = 4

# Generate a sequence of numbers
x = np.linspace(0, 20, 100)

# Plot the probability density function (PDF)
plt.plot(x, chi2.pdf(x, df))
plt.title('Chi-Squared Distribution')
plt.show()


from scipy.stats import t

# Define the degrees of freedom for the t-distribution
df = 10

# Generate a sequence of numbers
x = np.linspace(-5, 5, 100)

# Plot the probability density function (PDF)
plt.plot(x, t.pdf(x, df))
plt.title('t-Distribution')
plt.show()
