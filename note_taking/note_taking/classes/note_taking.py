# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:21:07 2017

@author: James Kinyua
"""
import sys

from note import Note

# Add the classes directory path to sys to import classes.
sys.path.append('../database')

from db import NoteDB

class NoteTaking:
    def __init__(self):
        self.db = NoteDB()
        
    def create_note(self, content):
        note = Note(content)
