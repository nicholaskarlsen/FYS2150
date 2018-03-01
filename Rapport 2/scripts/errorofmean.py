import numpy as np

L_a_hultafors = np.array([
    119.5, 119.5, 119.45, 119.4, 119.43, 119.4, 119.4, 119.45, 119.4,
    119.43
    ])

L_b_hultafors = np.array([
    119.6, 119.7, 119.6, 119.5, 119.55, 119.6, 119.5, 119.65, 119.6,
    119.55
    ])

L_a_laser = np.array([
    120.5, 119.6, 119.5, 119.4, 119.4, 119.68, 119.9, 130.6, 119.4
    ])

L_b_laser = np.array([
    120.6, 119.8, 119.7, 119.6, 119.6, 119.72, 119.7, 130.2, 119.5
    ])

def error_mean(x):
    "Eqn D. Page 24 squires"
    n = len(x)
    sigma = np.sqrt(float(np.sum(x**2) - 1.0/n * np.sum(x)**2)/(n - 1))
    sigma_m = np.sqrt(float(np.sum(x**2) - 1.0/n * np.sum(x)**2)/(n*(n - 1)))
    return sigma, sigma_m

if __name__ == '__main__':

    diff_hultfors = abs(L_a_hultafors - L_b_hultafors)
    diff_laser = abs(L_a_laser - L_b_laser)

    print np.mean(diff_hultfors), np.mean(diff_laser)
    print error_mean(abs(L_a_hultafors - L_b_hultafors))
    print error_mean(abs(L_a_laser - L_b_laser))

