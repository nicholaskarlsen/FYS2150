import numpy as np

def importdata(filename):
	infile = open(filename, 'r')
	lines = infile.readlines()
	data = []

	for line in lines:
		line = line.split()
		data.append(line)
	infile.close()

	for i in range(len(data)):
		for j in range(len(data[i])):
			data[i][j] = float(data[i][j])
	data = np.array(data)
	return data

def linear_fit(x, y):
    n = np.size(y)
    D = np.sum(x**2) - (1.0 / n) * np.sum(x)**2
    E = np.sum(x*y) - (1.0 / n) * np.sum(x) * np.sum(y)
    F = np.sum(y**2) - (1.0 / n) * np.sum(y)**2
    
    dm = np.sqrt(1.0 / (n - 2) * (D * F - E**2) / D**2)
    dc = np.sqrt(1.0 / (n - 2) * (float(D) / n + np.mean(x)) * ( (D*F - E**2) / (D**2) ))
    m = float(E) / D
    c = np.mean(y) - m*np.mean(x)
    return dm, dc, c, m

def mean_uncertainty(vals):
 	n = len(vals)
 	mean_uncertainty = np.sqrt((np.sum(vals**2) - (1.0 / n) * np.sum(vals)**2) / (n * (n - 1)))
 	return mean_uncertainty


if __name__ == '__main__':
	dat = importdata("maalinger_deformasjon.dat")

	m = dat[:, 0]
	h = dat[:, 1]

	d_alph, d_beta, beta, alph = linear_fit(m, h)

	tau=[4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
	tau = np.array(tau)

	k = 2.0 / (np.mean(tau) / (2 * np.pi))**2

	print mean_uncertainty(tau)

	print 4 * mean_uncertainty(tau) / np.mean(tau) * (1.0 / 1e-3)