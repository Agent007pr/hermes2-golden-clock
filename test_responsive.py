import unittest
import re

class TestResponsiveLayout(unittest.TestCase):
    def setUp(self):
        with open("index.html", "r", encoding="utf-8") as f:
            self.html = f.read()

    def test_lang_attribute(self):
        matches = re.findall(r'<html[^>]*\blang=["\']([a-z]+)["\']', self.html, re.IGNORECASE)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], "en")

    def test_clock_div(self):
        matches = re.findall(r'<div\s+id=["\']clock["\']', self.html, re.IGNORECASE)
        self.assertEqual(len(matches), 1)

    def test_animation_loop(self):
        interval_calls = len(re.findall(r'setInterval\s*\(', self.html))
        raf_calls = len(re.findall(r'requestAnimationFrame\s*\(', self.html))
        self.assertEqual(interval_calls + raf_calls, 1)

    def test_time_formatting_function(self):
        matches = re.findall(r'function\s+\w*(time|format|clock)\w*\s*\(', self.html, re.IGNORECASE)
        self.assertEqual(len(matches), 1)

    def test_viewport_meta_tag(self):
        # ac: AT2
        matches = re.findall(r'<meta\s+name=["\']viewport["\']', self.html, re.IGNORECASE)
        self.assertEqual(len(matches), 1)

    def test_responsive_sizing(self):
        # ac: AT2
        relative_units = len(re.findall(r'\d+(\.\d+)?%|\d+(\.\d+)?rem|\d+(\.\d+)?em|\d+(\.\d+)?vh|\d+(\.\d+)?vw', self.html))
        media_queries = len(re.findall(r'@media\s*\([^)]*max-width', self.html, re.IGNORECASE))
        self.assertEqual(relative_units + media_queries, 1)
