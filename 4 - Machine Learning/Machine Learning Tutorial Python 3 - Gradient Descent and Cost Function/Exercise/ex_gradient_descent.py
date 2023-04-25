import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002

    cost_previous = 0

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([value**2 for value in (y - y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost

        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))

    return m_curr, b_curr
