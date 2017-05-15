# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:21:07 2017

@author: James Kinyua
"""
import sys
import json
import csv

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
        # The note_id is not a digit.
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
            self.remaining = False
        else:
            print("There are no more notes to print.")
                
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
                # No note matches the query string.
                if len(self.found_notes) < 1:
                    print("Sorry no notes were found.")
                    return
                else:
                    try:
                        self.remaining = True
                        notes = self.found_notes[:limit]
                        self.remaining_notes = self.found_notes[limit:]
                        print("Note_id \tContent\n")
                        for note in notes:
                            print("{0} \t{1}".format(note.id, note.content))
                    except IndexError:
                        print("Cannot display notes if limit is greater than" + 
                        "notes")
                        return
            except ValueError:
                print('Invalid limit. Please enter a valid number.')
        else:
            notes = self.db.get_notes()
            print("Note_id \tContent\n")
            for note in notes:
                found = note.search(query_string)
                if found is not None:
                    print("{0} \t{1}".format(note.id, note.content))
                
    def delete_a_note(self, note_id):
        """
        Delete a note.
        """
        try:
            note_id = int(note_id)
            self.db.delete_note(note_id)
        except ValueError:
            print("Not a valid note id.")
                
    def export_to_json(self, filename):
        """
        Export notes to json format.
        """
        notes = self.db.get_notes()
        notes_dict = {}
        # Create a dictionary of the notes.
        for note in notes:
            notes_dict[note.id] = note.content
            
        print(notes_dict)
        # Create a json file
        with open(filename, 'w') as f_obj:
            json.dump(notes_dict, f_obj)
        print(filename, "was successfully created!")
        
    def import_from_json(self, filename):
        """
        Import notes from json file.
        """
        with open(filename) as f_obj:
            # Read the contents from the file.
            notes = json.load(f_obj)
        for note in notes:
            # Add the note to the database.
             self.create_note(note)
            
    def export_to_csv(self, filename):
        """
        Export notes to csv format.
        """
        notes = self.db.get_notes()
        # Pass newline agrument to avoid double spacing on windows.
        with open(filename, 'w', newline='') as f_obj:
            # Create a csv writer object.
            output_writer = csv.writer(f_obj)
            for note in notes:
                output_writer.writerow([note.id, note.content])
        print(filename, "was successfully created!")
            
        
    
