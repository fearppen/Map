class MapParams:
    def __init__(self):
        self.longitude = 37.530887
        self.latitude = 55.703118
        self.zoom = 15

    def zoom_up(self):
        self.zoom += 1

    def zoom_down(self):
        self.zoom -= 1

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom
