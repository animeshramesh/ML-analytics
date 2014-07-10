from utils import load_model
from sklearn import linear_model

clf = linear_model.LinearRegression()
training_data = load_model.load_model()

all_monthly_params = []
precipation_values = []
for year in training_data.keys():
    monthly_params = []
    annual_weather = training_data[year]
    for i in range(0, 11):
        cloud_cover = annual_weather.get_cloud_cover()[i]
        min_temp = annual_weather.get_min_temp()[i]
        rain = annual_weather.get_precipitation()[i]
        precipation_values.append(float(rain))
        x = list()
        x.append(float(cloud_cover))
        x.append(float(min_temp))
        x.append(float(rain))
        all_monthly_params.append(x)

clf.fit(all_monthly_params, precipation_values)
# equation is of the form -> Z = ax + by + c
Z = precipation_values[36]
print Z
a = clf.coef_[2]
b = clf.coef_[1]
c = clf.coef_[0]
x = all_monthly_params[36][0]
y = all_monthly_params[36][1]
print a*x + b*y + c
print clf.coef_