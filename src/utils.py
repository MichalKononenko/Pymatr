
import sympy as sym
import numpy as num

from sympy.matrices import *

def ewp(A,B, zeros_fun=zeros):
	(m,n) = A.shape
	(m2,n2)= B.shape
	if A.shape != B.shape:
		raise IncompatibleShape
	R= zeros_fun(m,n)
	for i in range(0,m):
		for j in range(0,n):
			R[i,j]=A[i,j]*B[i,j]	
	return R

def MId(d):
	''' Identity matrix '''
	m= eye(d)
	return m

def numerical(M, factor=1 ):
	sh=M.shape
	N=num.zeros((sh[0], sh[1]))
	for i in range(sh[0]):
		for j in range(sh[1]):
			N[i,j]= (factor*M[i,j]).evalf()
	return np.matrix(N)


import math
import random
import numpy as np
def simplexAlea(d):
	''' Uniform random variable on the standard simplex of dimension d-1 '''
	def rand():
		a= -np.log([ random.random() for x in range(d)]) 
		s= sum(a)
		a= a/s
		return a
	return rand	

def MarkovianIntegral(sampler, fun, eps=5e-2, n0=1000 ):
	''' Basic markovian sampler'''
	n=n0
	s1=sum(( fun(sampler()) for x in range(n)  ))/n
	s2=sum(( fun(sampler()) for x in range(n)  ))/n
	while( np.linalg.norm(s1-s2)> eps ):
		print ("norm, step {} :{}".format(n, np.linalg.norm(s1-s2))  )
		s1=(s1+s2)/2
		n*=2
		s2=sum(( fun(sampler()) for x in range(n) ))/n
	return (s1+s2)/2

def gaussian(xs, sigma2s):
	''' Gaussian distribution '''	
	xrs = [np.float64(x) for x in xs]
	def f(alphas):
		sigma2= np.float64( sum(alphas * sigma2s) )
		core= -np.power(xrs,2)/(2*sigma2)
		norm= math.sqrt(2*math.pi*sigma2)  
		return np.exp(core) / norm 
	return f
