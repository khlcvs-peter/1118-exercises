import unittest
import importlib.util
from decimal import Decimal

# 載入有空格和括號的檔案路徑為模組
spec = importlib.util.spec_from_file_location("mod1118", r"c:\Users\User\Downloads\lib_1118.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class Test1118(unittest.TestCase):
    def test_total(self):
        self.assertEqual(mod.compute_total_1_to_100(), 5050)

    def test_enumerate(self):
        self.assertEqual(mod.enumerate_list(['Mary', 'had']), [(0, 'Mary'), (1, 'had')])

    def test_compound(self):
        # 本金 1000，年利率 12%，兩個月後應為 1000 * 1.01 * 1.01 = 1020.1
        amounts = mod.compute_compound_amounts(Decimal('1000'), Decimal('12'), 2)
        self.assertEqual(amounts[-1].quantize(Decimal('0.01')), Decimal('1020.10'))

if __name__ == '__main__':
    unittest.main()
