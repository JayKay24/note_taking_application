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
        try: 
            for note in notes:
                if int(note_id) == note.id:
                    print(note.content)
                    break
            else:
                print("No note matches that id.")
        except ValueError:
            print("Invalid note id. Please enter a valid note id.")
    def list_notes(self, limit=None, next_notes=False):
        """
        List all the notes.
        """
        self.remaining_notes = None
        self.remaining = False
        try:
            if limit is not None:
                limit = int(limit)
                print("Note_id \tContent\n")
                try:
                    self.all_notes = self.db.get_notes()
                    # Notes are in the queue to be displayed.
                    self.remaining = True
                    notes = self.all_notes[:limit]
                    self.remaining_notes = self.all_notes[limit:]
                    for note in notes:
                        print("{0} \t{1}".format(note.id, note.content))
                except IndexError:
                    print("Cannot display notes if limit is greater than" + 
                    "notes")
                    return
            else:
                notes = self.db.get_notes()
                print("Note_id \tContent\n")
                for note in notes:
                    print("{0} \t{1}".format(note.id, note.content))
            
        except ValueError:
            print('Invalid limit. Please enter a valid number.')
            
    def next_notes(self):
        if self.remaining is True:
            
            for note in self.remaining_notes:
                print("{0} \t{1}".format(note.id, note.content))
                
    def search_notes(self, query_string, limit=None):
        """
        Search notes for string matching query_string.
        """
        self.remaining_notes = None
        if limit is not None:
            try:
                limit = int(limit)
                notes = self.db.get_notes()
                self.found_notes = []
                for note in notes:
                    found = note.search(query_string)
                    if found is not None:
                        self.found_notes.append(found)
                if len(self.found_notes) < 1:
                    print("Sorry no notes were found.")
                    return
                else:
                    try:
                        self.remaining = True
                        notes = self.found_notes[:limit]
                        self.remaining_notes = self.found_notes[limit:]
                        for note in notes:
                            print("{0} \t{1}".format(note.id, note.content))
                    except IndexError:
                        print("Cannot display notes if limit is greater than" + 
                        "notes")
                        return
            except ValueError:
                print('Invalid limit. Please enter a valid number.')
                
    def delete_a_note(self, note_id):
        """
        Delete a note.
        """
        try:
            note_id = int(note_id)
            self.db.delete_note(note_id)
        except ValueError:
            print("Not a valid note id.")
                
                    
        
    
