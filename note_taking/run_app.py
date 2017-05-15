# -*- coding: utf-8 -*-
"""
This example uses docopt with the built in cmd module to demonstrate an 
interactive command application.
Usage:
    note create_note <note_content>...
    note view_note <note_id>
    note delete_note <note_id>
    note list_notes [<limit>]
    note next
    note search_notes <query_string> [<limit>]
    note export_json <filename>
    note export_csv <filename>
    note (-i | --interactive)
    note (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""
import os
import sys
import cmd
from docopt import docopt, DocoptExit

from note_taking.classes.note_taking import NoteTaking

current_directory = os.getcwd()
os.chdir('./note_taking/files')
note = NoteTaking()
note.db.connect_db()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
    
class MyInteractive (cmd.Cmd):
    prompt = '(note) '
    file = None
    
    @docopt_cmd
    def do_create_note(self, args):
        """Usage: create_note <note_content>..."""
        
        content_list = args['<note_content>']
        content = ' '.join(content_list)
        note.create_note(content)
        
    @docopt_cmd
    def do_view_note(self, args):
        """Usage: view_note <note_id>"""
        
        note_id = args['<note_id>']
        note.view_note(note_id)
        
    @docopt_cmd
    def do_delete_note(self, args):
        """Usage: delete_note <note_id>"""
        
        note_id = args['<note_id>']
        note.delete_a_note(note_id)
        
    @docopt_cmd
    def do_list_notes(self, args):
        """Usage: list_notes [<limit>]"""
        
        limit = args['<limit>']
        note.list_notes(limit)
        
    @docopt_cmd
    def do_next(self, args):
        """Usage: next"""
        
        note.next_notes()
        
    @docopt_cmd
    def do_search_notes(self, args):
        """Usage: search_notes <query_string> [<limit>]"""
        
        query_string = args['<query_string>']
        limit = args['<limit>']
        note.search_notes(query_string, limit)
        
    @docopt_cmd
    def do_export_json(self, args):
        """Usage: export_json <filename>"""
        
        filename = args['<filename>']
        note.export_to_json(filename)
        
    @docopt_cmd
    def do_export_csv(self, args):
        """Usage: export_csv <filename>"""
        
        filename = args['<filename>']
        note.export_to_csv(filename)
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        
        print("Good Bye!")
        note.db.close_db()
        exit()      
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    
    MyInteractive().cmdloop()
print(opt)