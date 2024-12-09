import sys
import os
from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from antlr4.tree.Trees import Trees

def parse_file(file_path):
    """
    Parse a Python file using the generated ANTLR parser.
    
    Args:
        file_path (str): Path to the Python file to parse
    
    Returns:
        tuple: (success status, parse tree string)
    """
    # Check if file exists
    if not os.path.exists(file_path):
        return False, f"Error: File {file_path} not found"

    try:
        # Create input stream
        input_stream = FileStream(file_path)
        
        # Create lexer
        lexer = PythonLexer(input_stream)
        
        # Create token stream
        stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = PythonParser(stream)
        
        # Parse the file
        tree = parser.program()
        
        # Check for parsing errors
        if parser.getNumberOfSyntaxErrors() > 0:
            return False, f"Parsing failed with {parser.getNumberOfSyntaxErrors()} syntax errors"
        
        # Generate parse tree as string
        parse_tree_str = Trees.toStringTree(tree, recog=parser)
        
        return True, parse_tree_str
    
    except Exception as e:
        return False, f"An error occurred during parsing: {str(e)}"

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python parser.py <python_file_path>")
        sys.exit(1)
    
    # Get file path from command line
    file_path = sys.argv[1]
    
    # Parse the file
    success, result = parse_file(file_path)
    
    # Print parsing result
    if success:
        print(f"Parsing of {file_path}: SUCCESSFUL")
        
        # Generate parse tree output file
        output_file = f"{os.path.splitext(file_path)[0]}_parse_tree.txt"
        with open(output_file, 'w') as f:
            f.write(result)
        
        print(f"Parse tree written to {output_file}")
    else:
        print(f"Parsing of {file_path}: FAILED")
        print(result)

if __name__ == "__main__":
    main()