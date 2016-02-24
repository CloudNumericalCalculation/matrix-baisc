#coding: utf-8
from __future__ import division
import sys
import numpy as np

def getMatrixString(idx):
	A = data[idx].replace("\n", ";")
	while A[-1:] == ";":
		A = A[:-1]
	return A

data = input()
op = data["op"]
if op not in ["+", "-", "*"]:
	print "不存在`%s`这个运算符！" % (op)
	sys.exit(1)
try:
	A = np.matrix(getMatrixString("A"))
	B = np.matrix(getMatrixString("B"))
except:
	print "矩阵格式错误！"
	sys.exit(1)

try:
	if op == "+":
		C = A + B
	else:
		if op == "-":
			C = A - B
		else:
			C = A * B
except:
	print "运算错误！"
	sys.exit(2)

def to_latex_bmatrix(A):
	n, m = A.shape
	latexStr = "\\begin{bmatrix}"
	for i in range(0, n):
		for j in range(0, m - 1):
			latexStr += "%d&" % (A[i, j])
		latexStr += "%d\\\\\\\\" % (A[i, m - 1])
		# 由于markdown的缘故，所以需要输出4个`\`供markdown转义
	latexStr += "\end{bmatrix}"
	return latexStr

print "$$%s%s%s=%s$$\n\n" % (to_latex_bmatrix(A), op, to_latex_bmatrix(B), to_latex_bmatrix(C))
sys.exit(0)
