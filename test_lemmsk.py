#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lemmsk
import unittest


class TestSimpleLemmatization(unittest.TestCase):
    def test_lemmatization(self):
        self.assertEqual(lemmsk.lemmatize('kuraciemu'), 'kurací')

        self.assertTrue(lemmsk.is_lemma('kurací'))


if __name__ == '__main__':
    unittest.main()
