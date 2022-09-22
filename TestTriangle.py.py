# -*- coding: utf-8 -*-

import unittest
# import Triangle-1

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # def testRightTriangleA(self): 
    #     self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    # def testRightTriangleB(self): 
    #     self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles1(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral trinagle')

    def testEquilateralTriangles2(self):
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral', '7,7,7 should be equilateral trinagle')

    def testEquilateralTriangles3(self):
        self.assertEqual(classifyTriangle(15, 1, 15), 'Equilateral', '15,1,15 should be equilateral trinagle')

    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5),'Right', '3,4,5 should be Right triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 should be Right triangle')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right', '13,12,5 should be Right triangle')

    def testRightTriangle4(self):
        self.assertEqual(classifyTriangle(8, 6, 10), 'Right', '8,6,10 should be Right triangle')

    def testRightTriangle5(self):
        self.assertEqual(classifyTriangle(21, 6, 10), 'Right', '21,6,10 should be Right triangle')

    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(10, 11, 12),'Scalene','10,11,12 should be Scalene triangle')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1,2,3 should be Scalene triangle')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(100, 110, 112), 'Scalene', '100,110,112 should be Scalene triangle')

    def testScaleneTriangle4(self):
        self.assertEqual(classifyTriangle(10, 10, 12), 'Scalene', '10,10,12 should be Scalene triangle')

    def testIsocelesTriangle1(self):
        self.assertEqual(classifyTriangle(5, 5, 3),'Isoceles','5,5,3 should be a Isoceles triangle')

    def testIsocelesTriangle2(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isoceles', '4,6,6 should be a Isoceles triangle')

    def testIsocelesTriangle3(self):
        self.assertEqual(classifyTriangle(8, 6, 8), 'Isoceles', '8,6,8 should be a Isoceles triangle')

    def testIsocelesTriangle4(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isoceles', '6,6,4 should be a Isoceles triangle')

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1, 3, 5),'NotATriangle','1,3,5 NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(1, 4, 5), 'NotATriangle', '1,4,5 NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'NotATriangle', '1,0,1 NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(1, 17, 5), 'NotATriangle', '1,17,5 NotATriangle')

    def testInvalidInput1(self):
       self.assertEqual(classifyTriangle(-1, -1, -1),'InvalidInput','-1,-1,-1 is InvalidInput')

    def testInvalidInput2(self):
       self.assertEqual(classifyTriangle("200", "200", "200"),'InvalidInput','200,200,200 is InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

