# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:41:21 2017

@author: James Kinyua
"""
import unittest
import sys

# Add the classes directory path to sys to import classes.
sys.path.append('../classes')

from note import Note

class NoteTest(unittest.TestCase):
    def setUp(self):
        self.note1 = Note("Speedsters")
        
    def test_note_id_is_none(self):
        self.assertIsNone(self.note1.id)
        
    def test_note_search_returns_note_object(self):
        note = self.note1.search('Speed')
        self.assertEqual(type(self.note1), type(note), 
        "search method should return self if substring is in content")
        
    def test_note_search_returns_none_for_no_match(self):
        note = self.note1.search('Jay Garrick')
        self.assertIsNone(note, "should return none if no match is found")
        
