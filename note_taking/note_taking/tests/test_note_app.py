# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:55:23 2017

@author: Geoffrey.ngae
"""
import unittest

from test_note import NoteTest

def suite():
    """
    Return a composite testsuite.
    """
    note_suite = unittest.makeSuite(NoteTest)
    
    return unittest.TestSuite((note_suite,))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
