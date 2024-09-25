# -*- coding: utf-8 -*-
"""
Convert student Python file to a function with classes

@author: Glenn Bruns
"""

from argparse import ArgumentParser 
from pathlib import Path
import sys
import ast

def is_assignment_stmt(s):
    """ Return true is string s is a Python assignment statement. 
    This code is based on a suggestion from ChatGPT.  """
    
    try:
        # parse the string into an abstract syntax tree (AST)
        parsed = ast.parse(s, mode='exec')

        # check if any node in the AST is an ast.Assign node
        for node in ast.walk(parsed):
            if isinstance(node, ast.Assign):
                return True
            
        return False
    except SyntaxError:
        # If the line is not valid Python code, return False
        return False
    

class IndentPrinter:
    
    def __init__(self, indent_size=4):
        self.level = 0
        self.indent_size = indent_size
        self.content = ""
        
    def indent(self):
        """ Increase indentation level by 1. """
        
        self.level += 1
        
    def dedent(self):
        """ Decrease indentation level by 1. """
        
        self.level -= 1
        
    def printi(self, s=""):
        """ Print string s at the current indentation level."""
        
        self.content += (self.level*self.indent_size*' ')+s+'\n'
        
    def to_string(self):
        return self.content
        
        
class Submission:
    
    def __init__(self):
        self.imports = ''
        self.probs = []
        
    def to_class(self):
        """ Print this as a Python class. """
        
        printer = IndentPrinter()
        
        # imports
        for line in self.imports.splitlines():
            printer.printi(line)
        printer.printi()
        
        # functions
        printer.printi('class Problems:')
        printer.indent()
        for prob in self.probs:
            prob.to_function(printer)
            printer.printi()
            
        return printer.to_string()
    

class Problem:
    
    def __init__(self, prob_id):
        self.prob_id = prob_id
        self.assign = ''
        self.params = []
        self.body = ''
        
    def to_function(self, printer):
        """ Print this as a Python function. """
        
        printer.printi('@staticmethod')
        printer.printi('def prob_'+self.prob_id+'('+','.join(self.params)+'):')
        
        printer.indent()
        body_lines = self.body.splitlines()
        if len(body_lines) == 0:
            # no code submitted
            printer.printi('return None')
        else:
            body_is_assignment = is_assignment_stmt(body_lines[-1])
                
            if self.assign != '':
                # assignment statement
                if not body_is_assignment:
                    sys.exit(f'Error: problem {self.prob_id}: problem requires a statement but answer is an expression')
                for line in body_lines:
                    printer.printi(line)
                # it's important to use the assign variable here, because the
                # last line of the body might be a complicated assignment, like x[x < 0] = ...
                printer.printi('return '+self.assign)
            else:
                # expression
                if body_is_assignment:
                    sys.exit(f'Error: problem {self.prob_id}: problem requires an expression but answer is an assignment')
                for line in body_lines[:-1]:
                    printer.printi(line)
                printer.printi('_x = '+body_lines[-1])
                printer.printi('return _x')
        printer.dedent()
        
        
def parse_submission(filename):
  
    def syntax_error(line):
        raise RuntimeError("Error: syntax error: {}".format(line))
    
    submission = Submission()
    
    prob = None
    in_comment = False
    with open(filename, encoding="utf8") as f:
        try:
            for line in f:
                toks = str.split(line)
                if len(toks) > 0:    # ignore blank lines
                    if toks[0] == '"""':
                        # start or end of multi-line comment
                        in_comment = not in_comment
                        continue
                    if not in_comment:
                        if toks[0] == "#@":
                            if toks[1] == "problem":
                                if prob is not None:  
                                    # wrap up current problem
                                    submission.probs.append(prob)
                                    
                                # start new problem
                                prob_id = toks[2]
                                prob = Problem(prob_id)
                            elif toks[1] == "assign":
                                if prob is None:
                                    syntax_error(line)
                                prob.assign = toks[2]
                            elif toks[1] == "assume":
                                if prob is None:
                                    syntax_error(line)
                                prob.params = toks[2].split(",")
                        elif toks[0] == "##":
                            # no processing for now
                            pass
                        elif toks[0] == "#":
                            # plain Python comment
                            pass
                        else:
                            # code 
                            if prob is None:
                                # first problem not reached yet
                                submission.imports += line
                            else:
                                prob.body += line
                        
            # wrap up current problem
            submission.probs.append(prob)
                          
        except UnicodeDecodeError as e:
            print(e)
            
    return submission


def test_translate():
    infile  = "C:/Users/Glenn/Google Drive/CSUMB/Spring22/DS/homework/unit-testing/numpy-basics.py"
    outfile = "C:/Users/Glenn/Google Drive/CSUMB/Spring22/DS/homework/unit-testing/temp.py"
    translate(infile, outfile)


def translate(infile, outfile):
    """ Translate student reponses to methods. """
    
    submission = parse_submission(infile)
    prog = submission.to_class()
    
    py_file = open(outfile, 'w')
    _ = py_file.write(prog)
    py_file.close()    


def main():
    
    # parse command-line arguments
    parser = ArgumentParser()
    parser.add_argument("infile", help="a Python file with student responses")
    parser.add_argument("outfile", help="a Python file with response placed in methods")
    args = parser.parse_args()
    
    # command line inputs are interpreted relative to current working directory
    current_dir = Path.cwd()
    
    infile     = current_dir / args.infile
    outfile    = current_dir / args.outfile
    
    if infile == outfile:
        raise ValueError('error: input file name and output file name are the same')
    
    translate(infile, outfile)


if __name__ == '__main__':
    main()
