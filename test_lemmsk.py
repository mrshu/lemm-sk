#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lemmsk
import unittest


class TestSimpleLemmatization(unittest.TestCase):
    def test_lemmatization(self):
        self.assertEqual(lemmsk.lemmatize('kuraciemu'), 'kurací')
        self.assertEqual(lemmsk.lemmatize('kuracieho'), 'kurací')

        self.assertTrue(lemmsk.is_lemma('kurací'))
        self.assertFalse(lemmsk.is_lemma('kuraciemu'))
        self.assertFalse(lemmsk.is_lemma('kuracieho'))


if __name__ == '__main__':
    unittest.main()
