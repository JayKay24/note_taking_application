# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:00:31 2017

@author: James Kinyua
"""
import unittest

from classes.note import Note
from classes.note_taking import NoteTaking
from database.db import NoteDB

class NoteTakingTest(unittest.TestCase):
    def setUp(self):
        self.note1 = Note("Jay Garrick")
        self.note_taking = NoteTaking()
        self.note_db = NoteDB()
        
    def test_create_note(self):
        self.note_taking.create_note()
        # Connect to the database.
        self.note_db.connect_db()
        note_objects = self.note_db.get_notes()
        # Close the database connection.
        self.note_db.close_db()
        note_names = [note.content for note in note_objects]
        self.assertIn(self.note1.content, note_names, 
        "note should be included in the database")
        
    def test_view_note_returns_1(self):
        # Connect to the database.
        self.note_db.connect_db()
        note_objects = self.note_db.get_notes()
        # Close the database connection.
        self.note_db.close_db()
        note_ids = [note.id for note in note_objects]
        return_value = self.note_taking.view_note(note_ids[0])
        self.assertEqual(return_value, 1, 
        "should return 1 if note is found in the database")
        
