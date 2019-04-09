import os
import unittest
import culpa

def here(path):
    here_ = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here_, path)


class TestCulpa(unittest.TestCase):

    def test_columns(self):
        act = culpa.read_file(here('test.xlsx'))
        exp = ['alpha', 'beta', 'charlie', 'delta', 'echo']
        self.assertEqual(exp, act)

    def test_col_content(self):
        act = culpa.read_col(here('test.xlsx'), 'charlie')
        exp = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
        self.assertEqual(exp, act)

if __name__ == '__main__':
    unittest.main()
