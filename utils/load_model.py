__author__ = 'Animesh'

from utils import parser
import model


def load_model():
    min_temp = parser.parse_csv("datasets/min_temp.csv")
    cloud_cover = parser.parse_csv("datasets/cloud_cover.csv")
    precipitation = parser.parse_csv("datasets/precipitation.csv")
    vp = parser.parse_csv("datasets/vp.csv")
    ground_frost = parser.parse_csv("datasets/ground_frost.csv")
    wet_day_freq = parser.parse_csv("datasets/wet_day_freq.csv")
    years = min_temp.keys()
    weather = []
    for year in years:
        yearly_params = list()
        for i in range(0, 11):
            monthly_params = list()
            monthly_params.append(float(min_temp[year][i]))
            monthly_params.append(float(cloud_cover[year][i]))
            monthly_params.append(float(vp[year][i]))
            monthly_params.append(float(wet_day_freq[year][i]))
            monthly_params.append(float(ground_frost[year][i]))
            monthly_params.append(float(precipitation[year][i]))
            yearly_params.append(monthly_params)
        weather.extend(yearly_params)
    return weather

