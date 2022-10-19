import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def poissons(lbd, data):

    lbd = lbd*1.0
    if lbd < 0 or data.any() < 0:
        print("Invalid parameters")
        return -1

    data.sort()
    x = data

    facts = {0:1.0}
    fact = 1
    for f in range(1, data[len(data)-1]+1):
        fact = fact*f*1.0
        facts[f] = fact

    y = []

    for i in x:
        y.append((2.718**(-lbd) * lbd**i)/facts[i])

    plt.title("Poisson's Distribution")
    plt.xlabel("Random Variable")
    plt.ylabel("Probablity")
    plt.axvspan(lbd-1, lbd, alpha = 0.5)
    plt.axvline(lbd)
    plt.plot(x, y)
    plt.show()

def normal(data):

    if data.any() < 0:
        print("Invalid parameters")
        return -1

    data = np.array(data)

    plt.title("Normal Distribution")
    plt.plot(data, norm.pdf(data, np.mean(data), np.std(data)))
    plt.xlabel("Data")
    plt.ylabel("Probablity")
    plt.axvline(np.mean(data))
    plt.xticks(np.arange(np.mean(data) - 3*np.std(data), np.mean(data) + 3*np.std(data), np.std(data)/2))
    plt.show()

def uniform(data, a, b):

    if data.any() < 0:
        print("Invalid parameters")
        return -1

    y = [0]*len(data)
    for x in range(len(data)):
        if data[x] > a and data[x] < b:
            y[x] = 1/(b-a)

    plt.title("Uniform Distribution")
    plt.plot(data, y)
    plt.xlabel("Data")
    plt.ylabel("Probablity")
    plt.show()
    
poissons(7, np.arange(1, 20, 2))
normal(np.arange(1, 20, 2))
uniform(np.arange(1, 20, 2), 12, 17.5)