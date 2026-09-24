import math
import unittest

from secret_of_a_half.half_bifurcation_moire import (T, iterate_closed, iterate_direct, plus_half, minus_half, moire_identity)

class HalfBifurcationMoireTests(unittest.TestCase):
    def test_closed_iterate(self):
        for x in (-0.5,0.5,1.25,-3.0):
            for n in range(8):
                self.assertAlmostEqual(iterate_closed(x,n),iterate_direct(x,n),places=12)
    def test_half_bifurcation(self):
        self.assertEqual(T(-0.5),0.0)
        self.assertEqual(T(0.5),2.0)
    def test_positive_branch(self):
        self.assertEqual([int(plus_half(n)) for n in range(1,7)],[2,5,11,23,47,95])
    def test_negative_branch(self):
        self.assertEqual([int(minus_half(n)) for n in range(1,7)],[0,1,3,7,15,31])
    def test_moire_identity(self):
        d,f=moire_identity(0.17,2.01)
        self.assertLess(abs(d-f),1e-12)
    def test_antiphase(self):
        self.assertLess(abs(complex(math.cos(.37),math.sin(.37))+complex(math.cos(.37+math.pi),math.sin(.37+math.pi))),1e-12)

if __name__=="__main__": unittest.main()
