import numpy as np
from matplotlib import pyplot as plt


def Kalman_Filter():
	delta_t = 1

	F =  np.matrix([[1,delta_t],[0,1]])
	G = np.matrix([[0],[delta_t]])
	P = np.matrix([[0,0],[0,0]])
	x = np.matrix([[0],[0]])
	r = 0.1
	q = 0.1
	Q = np.matrix([[0,0],[0,q*q]])
	R = r*r
	H = np.matrix([[1,0]])
	measurements = 1000
	u = np.random.normal(0,1,measurements)
	mx = np.random.normal(0,r,measurements)
	I = np.eye(2)
	pos = []
	vel = []

	for n in range(measurements):
		x = F*x + G*u[n]
		P = F*P*F.T + Q

		S = H*P*H.T + R
		K = (P*H.T)*np.linalg.pinv(S)

		Z = mx[n]
		y = Z - (H*x)
		x = x + (K*y)

		P = (I - (K*H))*P
		
		pos.append(x[0,0])
		vel.append(x[1,0])
	plt.plot(pos)
	plt.show()

Kalman_Filter()
