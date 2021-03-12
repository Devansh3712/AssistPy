'''
Testing play module
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
import packages.play as play

class TestSearch(unittest.TestCase):

    def test_search(self):

        url     = play.Search("torikago").get_link()
        result  = "https://www.youtube.com/watch?v=VD_JhspDBIg"
        self.assertEqual(url, result)

if __name__ == "__main__":
    unittest.main()

'''
AssistPy
Devansh Singh, 2021
'''