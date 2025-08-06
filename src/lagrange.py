from polynomial import Polynomial
from finitefield import GF

class Lagrange:

    def __init__(self, field):
        self.field = field

    def lagrange_basis(self, points : list[list], iteration):
        field = self.field
        basi : list[Polynomial] = []
        xs  = [x for x in range(len(points)) if x!=iteration]
        for x in xs:
            basi.append(Polynomial([1, -points[x][0]], field)
                        * Polynomial([(points[iteration][0]-points[x][0]).inverse()], field))
        final_basis = Polynomial([1], field)
        for basis in basi:
            final_basis *= basis
        return final_basis * Polynomial([points[iteration][1]], field)

    def interpolate(self, points : list[list]):
        px = [int(t[0]) for t in points]
        if len(set(px)) != len(px):
            raise IndexError("All points must have a unique X value! >:(")
        f = self.field
        final_polynomial = Polynomial([0], f)
        for i in range(len(points)):
            final_polynomial += self.lagrange_basis(points, i)
        return final_polynomial