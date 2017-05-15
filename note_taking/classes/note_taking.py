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
    """
    Class to create NoteTaking objects in the application Note Taking
    
    :ivar object db: A database object establishing a connection.
    """
    def __init__(self):
        self.db = NoteDB()
        
    def create_note(self, content):
        """
        Create a note.
        
        :arg string content: A string to pass to Note object.
        """
        note = Note(content)
        self.db.add_note(note)
        
    def view_note(self, note_id):
        """
        View contents of a note.
        
        :arg string note_id: A digit to be converted to an integer to establish
                    comparison.
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
    def list_notes(self, limit=None):
        """
        List all the notes.
        
        :arg int limit: An integer to limit the results to be displayed.
        
        :ivar list remaining_notes: A list to hold remaining notes after a 
                limit was passed.
                
        :ivar boolean remaining: A flag to indicate whether or not there are
                remaining notes left.
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
        """
        Display the next notes after a limit is reached.
        """
        if self.remaining is True:
            for note in self.remaining_notes:
                print("{0} \t{1}".format(note.id, note.content))
            self.remaining = False
        else:
            print("There are no more notes to print.")
                
    def search_notes(self, query_string, limit=None):
        """
        Search notes for string matching query_string.
        
        :arg string query_string: A string to determine if a note exists.
        :arg int limit: An integer to limit the notes to be displayed.
        
        :ivar list found_notes: A list to hold all the notes that match the
                query_string.
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
        
        :arg string note_id: A digit to be converted to an integer to
                establish comparison.
        """
        try:
            note_id = int(note_id)
            self.db.delete_note(note_id)
        except ValueError:
            print("Not a valid note id.")
                
    def export_to_json(self, filename):
        """
        Export notes to json format.
        
        :arg string filename: A string containing the name of a file.
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
        
        :arg string filename: A string containing the name of a file.
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
        
        :arg string filename: A string containing the name of a file.
        """
        notes = self.db.get_notes()
        # Pass newline agrument to avoid double spacing on windows.
        with open(filename, 'w', newline='') as f_obj:
            # Create a csv writer object.
            output_writer = csv.writer(f_obj)
            for note in notes:
                output_writer.writerow([note.id, note.content])
        print(filename, "was successfully created!")
            
    def import_from_csv(self, filename):
        """
        Import notes from csv format.
        
        :arg string filename: A string containing the name of a file.
        """
        # Read the contents from the file.
        with open(filename) as f_obj:
            input_reader = csv.reader(f_obj)
            for row in input_reader:
                # input_reader is a list of rows.
                for item in row:
                    # Add the note to the database.
                    self.create_note(item)
                    
            
        
    
