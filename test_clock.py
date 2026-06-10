import re
import unittest

class TestClockDisplay(unittest.TestCase):
    def setUp(self):
        with open('index.html', 'r', encoding='utf-8') as f:
            self.html = f.read()

    def test_ac1_clock_element(self):
        # ac: AT1
        match = re.search(r'id=["\']clock["\']', self.html)
        self.assertEqual(match.group(0), 'id="clock"')

    def test_ac1_date_element(self):
        # ac: AT1
        match = re.search(r'id=["\']date["\']', self.html)
        self.assertEqual(match.group(0), 'id="date"')

    def test_ac1_viewport_meta(self):
        # ac: AT1
        match = re.search(r'name=["\']viewport["\']', self.html)
        self.assertEqual(match.group(0), 'name="viewport"')

    def test_ac1_lang_attr(self):
        # ac: AT1
        match = re.search(r'lang=["\']en["\']', self.html)
        self.assertEqual(match.group(0), 'lang="en"')

    def test_ac1_time_formatting(self):
        # ac: AT1
        match = re.search(r'\.padStart\(\s*2\s*,\s*["\']0["\']\s*\)', self.html)
        self.assertEqual(match.group(0), '.padStart(2, "0")')

    def test_ac1_update_interval(self):
        # ac: AT1
        match = re.search(r'setInterval\s*\([^,]+,\s*(\d+)\s*\)', self.html)
        self.assertEqual(match.group(1), '1000')

    def test_ac1_date_logic(self):
        # ac: AT1
        match = re.search(r'getMonth\(\)\s*\+\s*1', self.html)
        self.assertEqual(match.group(0), 'getMonth() + 1')

if __name__ == '__main__':
    unittest.main()
