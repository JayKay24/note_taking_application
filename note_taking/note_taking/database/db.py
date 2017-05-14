# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:57:08 2017

@author: James Kinyua
"""
import sys
import sqlite3

from contextlib import closing

# Add the classes directory path to sys to import classes.
sys.path.append('../classes')

from note import Note
DB = 'note_taking.sqlite'

class NoteDB:
    def __init__(self):
        # Define a database connection object.
        self.conn = None
        
    def connect_db(self):
        """
        Connect to the database.
        """
        if not self.conn:
            # Connect to the database and return a connection
            # object.
            self.conn = sqlite3.connect(DB)
            # Access the results set using names like a dictionary.
            self.conn.row_factory = sqlite3.Row
            
    def close_db(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            
    def _make_note(self, row):
        """
        Create a Note object using a row from the results set.
        """
        return Note(row['content'], row['note_id'])
        
    def get_notes(self):
        """
        Return a list of Note objects
        """
        query = '''SELECT note_id, content FROM notes'''
        # Use a cursor object to execute the SQL statements.
        with closing(self.conn.cursor()) as c:
            c.execute(query)
            results = c.fetchall()
            
        notes = []
        for row in results:
            notes.append(self._make_note(row))
        return notes
        
    def get_note(self, note):
        """
        Return a single note from the database.
        """
        query = '''SELECT note_id, content FROM notes
                WHERE note_id=?'''
        with closing(self.conn.cursor()) as c:
            c.execute(query, (note.id,))
            row = c.fetchone()
        
        note = self._make_note(row)
        return note
        
    def add_note(self, note):
        """
        Add a note to the database.
        """
        sql = '''INSERT INTO notes(content) VALUES (?)'''
        with closing(self.conn.cursor()) as c:
            c.execute(sql, (note.content,))
            self.conn.commit()
            print("Note successfully created!")
        
    def delete_note(self, note):
        """
        Delete a note from the database.
        """
        sql = '''DELETE FROM notes WHERE note_id=?'''
        with closing(self.conn.cursor()) as c:
            c.execute(sql, (note.id,))
            self.conn.commit()
            print("Note successfully deleted!")
            
