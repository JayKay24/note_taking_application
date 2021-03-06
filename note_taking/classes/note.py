# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:59:58 2017

@author: James Kinyua
"""
class Note:
    """
    Class to create Note objects in the application note_taking
    
    :arg string content: Text assigned to the attribute content.
    :arg int id: A number assigned to the attribute id.
    
    :ivar int id: A number to match the database note id.
    :ivar string content: Text containing the note's content.
    """
    def __init__(self, content, id=None):
        self.id = id
        self.content = content
        
    def search(self, query_string):
        """
        Return self if query_string is found in the note's content
        
        :arg string query_string: Text to find in the note's content
        """
        if query_string in self.content:
            return self
