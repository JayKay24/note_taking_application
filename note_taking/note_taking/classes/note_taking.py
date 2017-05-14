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
        self.notes = None
        self.s_notes = None
        
    def create_note(self, content):
        """
        Create a note.
        """
        note = Note(content)
        self.db.add_note(note)
        
    def view_note(self, note_id):
        """
        View contents of a note.
        """
        notes = self.db.get_notes()
        for note in notes:
            if note_id == note.id:
                print(note.content)
        else:
            print("No note matches that id.")
    def list_notes(self, limit=None):
        """
        List all the notes.
        """
        if self.notes is None or len(self.notes) < 1:
            self.notes = self.db.get_notes()
        if limit is not None:
            try:
                if len(self.notes) > int(limit):
                    # Print only up to the note limit.
                    for note in self.notes[:limit]:
                        print(note.id, note.content)
                    # Set the remaining notes that haven't been displayed yet.
                    self.notes = self.notes[limit:]
                else:
                    # Print all the notes.
                    for note in self.notes:
                        print(note.id, note.content)
            except ValueError:
                print("Invalid limit. Please enter a valid number.")
                return
        else:
            # Print all the notes.
            for note in self.notes:
                print(note.id, note.content)
                
    def search_notes(self, query_string, limit=None):
        """
        Search notes for string matching query_string.
        """
        if self.s_notes is None or len(self.s_notes) < 1:
            self.s_notes = self.db.get_notes()
        
        if limit is not None:
            try:
                if len(self.s_notes) > int(limit):
                    # Print only up to the note limit.
                    for note in self.s_notes[:limit]:
                        print(note.id, note.content)
                    # Set the remaining notes that haven't been displayed yet.
                    self.s_notes = self.s_notes[limit:]
                else:
                    # Print all the notes.
                    for note in self.s_notes:
                        print(note.id, note.content)
            except ValueError:
                print("Invalid limit. Please enter a valid number.")
                return
        else:
            # Print all the notes.
            for note in self.s_notes:
                print(note.id, note.content)
                
                    
        
    
