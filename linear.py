# m = slope
# b = y-intercept
y_predicted = [m * x + b for x in x]

# loss is sum of sqaured vertical distances b/w predicted and actual values
total_loss = 0
total_loss += [(y[i] - y_predicted[i]) ** 2 for i in range(len(y))]

# gradient descent for parameters
def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
        diff += y[i] - (m * x[i] + b)

    b_gradient = (-2 / N) * diff
    return b_gradient

def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
        diff += x[i] * (y[i] - (m * x[i] + b))
    m_gradient = (-2 / N) * diff
    return m_gradient

# step gradient
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

# gradient decent
def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    for _ in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)
    return [b, m]