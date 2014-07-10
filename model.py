__author__ = 'Animesh'


class Model:

    def __init__(self):
        self.min_temp = []
        self.max_temp = []
        self.avg_temp = []
        self.cloud_cover = []
        self.vapour_pressure = []
        self.precipitation = []

    def set_min_temp(self, min_temp):
        self.min_temp = min_temp

    def set_precipitation(self, x):
        self.precipitation = x

    def set_max_temp(self, max_temp):
        self.max_temp = max_temp

    def set_avg_temp(self, avg_temp):
        self.avg_temp = avg_temp

    def set_cloud_cover(self, cloud_cover):
        self.cloud_cover = cloud_cover

    def set_vapour_pressure(self, vapour_pressure):
        self.vapour_pressure = vapour_pressure

    def get_min_temp(self):
        return self.min_temp

    def get_max_temp(self):
        return self.max_temp

    def get_avg_temp(self):
        return self.avg_temp

    def get_cloud_cover(self):
        return self.cloud_cover

    def get_vapour_pressure(self):
        return self.vapour_pressure

    def get_precipitation(self):
        return self.precipitation