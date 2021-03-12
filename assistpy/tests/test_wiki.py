'''
Testing wiki module
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import packages.wiki as wiki
import unittest

class TestSearch(unittest.TestCase):

    def test_search(self):
        query  = wiki.Search("Microsoft").wiki_search()
        result = "Microsoft Corporation (, ) is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services."
        self.assertEqual(query, result)

if __name__ == "__main__":
    unittest.main()

'''
AssistPy
Devansh Singh, 2021
'''