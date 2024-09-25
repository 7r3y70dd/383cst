# -*- coding: utf-8 -*-
"""

Unit tests for Lyft bike sharing homework.

@author: Glenn Bruns
"""

import unittest
import numpy as np
import pandas as pd
import importlib
from translate_to_functions import translate

def main():
    
    translate("bike-sharing.py", "bike-sharing-funcs.py")
    
    # import module dynamically; make sure module system finds new module
    importlib.invalidate_caches()  
    funcs = importlib.import_module("bike-sharing-funcs")
    problems = getattr(funcs, 'Problems')

    df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/lyft-small.csv')
    age_groups = [18, 25, 35, 50, 100]
    group_names = ['18-25', '25-35', '35-50', '>50']

    class Tests(unittest.TestCase):

        def test6(self):
            x = problems.prob_6(df)
            self.assertIsInstance(x, int)
            self.assertEqual(x, 19997)

        def test7(self):
            x = problems.prob_7(df)
            self.assertEqual(len(x), 14)
            self.assertEqual(x[0], 'trip_duration_sec')
            self.assertEqual(x[13], 'BART')

        def test8(self):
            x = problems.prob_8(df)
            self.assertAlmostEqual(x, 20.6, delta=0.1)

        def test9(self):
            x = problems.prob_9(df)
            self.assertAlmostEqual(x, 9.0, delta=0.1)

        def test12(self):
            x = problems.prob_12(df)
            self.assertIsInstance(x, pd.DataFrame)
            self.assertTupleEqual(x.shape, (10,4))
            self.assertEqual(x.iloc[3,1], 24)

        def test14(self):
            x = problems.prob_14(df)
            self.assertIsInstance(x, float)
            self.assertAlmostEqual(x, 0.871, delta=0.01)

        def test15(self):
            x = problems.prob_15(df)
            self.assertIsInstance(x, float)
            self.assertAlmostEqual(x, 0.0081, delta=0.0005)

        def test18(self):
            x = problems.prob_18(df)
            self.assertIsInstance(x, float)
            self.assertAlmostEqual(x, 0.1422, delta=0.001)

        def test19(self):
            x = problems.prob_19(df)
            self.assertIsInstance(x, float)
            self.assertAlmostEqual(x, 0.216, delta=0.005)

        def test20(self):
            x = problems.prob_20(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 2)
            self.assertEqual(x.values[0], 17413)
            self.assertEqual(x.index[1], 'Customer')

        def test22(self):
            x = problems.prob_22(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 4)
            self.assertAlmostEqual(x.values[0], 0.4787, delta=0.005)
            self.assertEqual(x.index[3], '>50')

        def test23(self):
            x = problems.prob_23(df, group_names)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 4)
            self.assertAlmostEqual(x.values[0], 0.1719, delta=0.005)
            self.assertEqual(x.index[0], '18-25')
        
        def test26(self):
            x = problems.prob_26(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 20)
            self.assertEqual(x.sum(), 546)
            self.assertEqual(x.values[0], 40)
            self.assertEqual(x.index[0][0], 'San Francisco Ferry Building (Harry Bridges Plaza)')

        def test27(self):
            x = problems.prob_27(df)
            self.assertIsInstance(x, pd.Index)
            
        def test28(self):
            x = problems.prob_28(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 4)
            self.assertAlmostEqual(x.sum(), 48.6, delta=0.2)
            self.assertAlmostEqual(x.values[0], 12.27, delta=0.1)
            self.assertEqual(x.index[0], '18-25')

        def test31(self):
            x = problems.prob_31(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 3)
            self.assertAlmostEqual(x.sum(), 30.0, delta=0.2)
            self.assertAlmostEqual(x.values[0], 10.0, delta=0.1)
            self.assertEqual(x.index[0], 'Female')

        def test32(self):
            x = problems.prob_32(df)
            self.assertIsInstance(x, pd.Series)
            self.assertEqual(x.size, 12)
            self.assertAlmostEqual(x.sum(), 117.0, delta=0.5)
            self.assertAlmostEqual(x.values[0], 10.0, delta=0.1)
            self.assertTupleEqual(x.index[0], ('Female', '18-25'))
            self.assertTupleEqual(x.index[1], ('Female', '25-35'))

        def test33(self):
            x = problems.prob_33(df)
            self.assertIsInstance(x, pd.DataFrame)
            self.assertTupleEqual(x.shape, (4, 2))
            self.assertAlmostEqual(x.iloc[0]['mean'], 12.27, delta=0.1)
            self.assertAlmostEqual(x.iloc[0]['median'], 8.0, delta=0.1)

        def test35(self):
            x = problems.prob_35(df)
            self.assertIsInstance(x, pd.Series)
            self.assertTupleEqual(x.shape, (2,))
            self.assertAlmostEqual(x.sum(), 1.76, delta=0.03)
            self.assertAlmostEqual(x.values[0], 0.868, delta=0.05)
            self.assertEqual(x.index[0], False)

        def test36(self):
            x = problems.prob_36(df, pd.Index(['15->6', '81->15', '196->182', '6->16']))
            self.assertIsInstance(x, pd.Series)
            self.assertTupleEqual(x.shape, (4,))
            self.assertAlmostEqual(x.sum(), 27.5, delta=0.3)
            self.assertAlmostEqual(x.values[0], 10.0, delta=0.2)
            self.assertEqual(x.index[0], '81->15')

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
