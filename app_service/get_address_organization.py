from services.i_organiztion_service import IOrgService
import math


class GetAddressOrganization:
    def __init__(self, service: IOrgService):
        self.service = service

    def dist(self, coords1, coords2):
        coef1 = 111000
        coef = math.cos(math.radians(coords1[1] + coords2[1]) / 2.)
        dx = abs(coords1[0] - coords2[0]) * coef * coef1
        dy = abs(coords1[1] - coords2[1]) * coef1
        return int((dx ** 2 + dy ** 2) ** 0.5)

    def execute_organization(self, param, longitude, latitude):
        organizations = param['features']
        for i in range(len(organizations)):
            org = organizations[i]['properties']['CompanyMetaData']['address'] + \
                       organizations[i]['properties']['CompanyMetaData']['Categories'][0]['name']
            x, y = organizations[i]['geometry']['coordinates'][0],\
                   organizations[i]['geometry']['coordinates'][1]
            if self.dist((longitude, latitude), (x, y)) <= 50:
                return organizations[i]['properties']['CompanyMetaData']['address'] + " " + \
                       organizations[i]['properties']['CompanyMetaData']['Categories'][0]['name']
