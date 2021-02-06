import math


class MapParams:
    LAT_STEP = 0.008
    LON_STEP = 0.02

    def __init__(self):
        self.start_longitude = 37.530887
        self.longitude = 37.530887
        self.start_latitude = 55.703118
        self.latitude = 55.703118
        self.zoom = 15
        self.type_map = 'map'

    def zoom_up(self):
        self.zoom += 1

    def zoom_down(self):
        self.zoom -= 1

    def left(self):
        self.longitude -= self.LON_STEP * math.pow(2, 15 - self.zoom)

    def right(self):
        self.longitude += self.LON_STEP * math.pow(2, 15 - self.zoom)

    def up(self):
        self.latitude += self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def down(self):
        self.latitude -= self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def set_longitude(self, longitude):
        self.longitude = longitude
        self.start_longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude
        self.start_latitude = latitude

    def change_type_map(self):
        self.type_map = 'map'

    def change_type_sat(self):
        self.type_map = 'sat'

    def change_type_sat_skl(self):
        self.type_map = 'sat,skl'

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom

    def get_type_map(self):
        return self.type_map

    def get_start_longitude(self):
        return self.start_longitude

    def get_start_latitude(self):
        return self.start_latitude
