# m = slope
# b = y-intercept
y_predicted = [m * x + b for x in x]\

#loss is sum of sqaured vertical distances b/w predicted and actual values
total_loss = 0
total_loss += [(y[i] - y_predicted[i]) ** 2 for i in range(len(y))]

