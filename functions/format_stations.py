import numpy as np


def polygon_area(polygon: []) -> float:
    # CALCULATE AREA OF AN POLYGON
    area = 0.
    positive = 0.
    negative = 0.

    for i, dot in enumerate(polygon):
        if i > 0:
            for j, value in enumerate(dot):
                if j > 0:
                    positive += polygon[i - 1][j - 1] * polygon[i][j]

    for i, dot in enumerate(polygon):
        if i > 0:
            for j, value in enumerate(dot):
                if j > 0:
                    negative += polygon[i - 1][j] * polygon[i][j - 1]

    return np.abs((positive - negative) / 2)


def format_stations(data: {}) -> {}:
    stations = {}
    for key, dots in data.items():
        dots_array = []

        for dot in dots:
            vertical = dot['vertical']
            transversal = dot['transversal']

            dots_array.append([vertical, transversal])

        area = polygon_area(dots_array)
        baliza = {
            'area': 2 * area,
            'dots': dots_array,
            'longitudinal': dots[0]['longitudinal']
        }
        stations[key] = baliza

    return (stations)