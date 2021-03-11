'''
Testing wiki module
'''

import wiki
import unittest

class TestSearch(unittest.TestCase):

    def search(self):
        query  = wiki.Search("Microsoft").wiki_search()
        result = "Microsoft Corporation ( MY-kroh-soft) is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services."
        self.assertEqual(query, result)

if __name__ == "__main__":
    unittest.main()