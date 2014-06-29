from scipy import stats
from utils import parser, math
import sys

precipitation_data = parser.parse_csv(sys.argv[1])
monthly_precipitation_training = parser.get_monthly_data(precipitation_data, 1901, 1990, 7)

x = range(len(monthly_precipitation_training))
y = map(float, monthly_precipitation_training)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print std_err
print math.get_y(slope, intercept, 1)

test_data = parser.get_monthly_data(precipitation_data, 1991, 2001, 7)

test_data = map(float, test_data)
computed_data = []
for val in test_data:
    computed_data.append(math.get_y(slope, intercept, val))
error = math.get_error(test_data, computed_data)
print error