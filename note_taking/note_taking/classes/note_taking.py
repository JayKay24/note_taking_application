# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:21:07 2017

@author: James Kinyua
"""
import sys

from .note import Note

# Add the database directory path to sys to import db.
sys.path.append('../')

from database.db import NoteDB

class NoteTaking:
    def __init__(self):
        self.db = NoteDB()
        self.notes = None
        self.s_notes = []
        
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
        if len(self.s_notes) < 1:
            notes = self.db.get_notes()
            for note in notes:
                found = note.search(query_string)
                # The note was found.
                if found is not None:
                    self.s_notes.append(found)
        
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
                
    def delete_a_note(self, note_id):
        """
        Delete a note.
        """
        try:
            note_id = int(note_id)
            self.db.delete_note(note_id)
        except ValueError:
            print("Not a valid note id.")
                
                    
        
    
