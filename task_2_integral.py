import numpy as np
import scipy.integrate as spi
from task_2_graph import func, a, b, y_min, y_max

# analytical integral calculation
def analytical_integral(func, a, b):
     result, _ = spi.quad(func, a, b)
     return result

# monte-carlo
def monte_carlo_integral(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area

if __name__ == "__main__":
    result = analytical_integral(func, a, b)  
    mc_result = monte_carlo_integral(func, a, b, y_min, y_max, 1500000)
    print(f"\nAnalytical integral: {result:.5f}\n \nMonte Carlo integral: {mc_result:.5f}\n")