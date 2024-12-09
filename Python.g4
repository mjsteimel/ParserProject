grammar Python;

// Parser Rules
program
    : (statement | NEWLINE)* EOF
    ;

statement
    : simple_stmt
    | compound_stmt
    ;

simple_stmt
    : (assignment_stmt 
     | expr 
     | break_stmt 
     | continue_stmt) NEWLINE?
    ;

compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    ;

// Control Flow Statements
break_stmt
    : BREAK
    ;

continue_stmt
    : CONTINUE
    ;

if_stmt
    : IF condition COLON NEWLINE?
      statement*
      elif_part*
      else_part?
    ;

elif_part
    : ELIF condition COLON NEWLINE?
      statement*
    ;

else_part
    : ELSE COLON NEWLINE?
      statement*
    ;

while_stmt
    : WHILE condition COLON NEWLINE?
      statement*
    ;

for_stmt
    : FOR NAME IN (expr | range_call) COLON NEWLINE?
      statement*
    ;

// Condition and Logical Expressions
condition
    : LPAREN condition RPAREN
    | or_condition
    ;

or_condition
    : and_condition (OR and_condition)*
    ;

and_condition
    : not_condition (AND not_condition)*
    ;

not_condition
    : NOT? (comparison | LPAREN condition RPAREN)
    ;

comparison
    : expr comparison_operator expr
    | expr
    ;

comparison_operator
    : LT
    | LTE
    | GT
    | GTE
    | EQ
    | NEQ
    ;

// Assignments and Expressions
assignment_stmt
    : NAME assignment_operator expr
    ;

assignment_operator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    ;

expr
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((MULT | DIV | MOD) factor)*
    ;

factor
    : PLUS factor
    | MINUS factor
    | atom
    ;

atom
    : NAME
    | NUMBER
    | STRING
    | BOOLEAN
    | array
    | function_call
    | range_call
    | LPAREN expr RPAREN
    ;

// Additional Support
array
    : LBRACK (array_element (',' array_element)*)? RBRACK
    ;

array_element
    : NUMBER
    | STRING
    | NAME
    ;

function_call
    : NAME LPAREN (expr (',' expr)*)? RPAREN
    ;

range_call
    : RANGE LPAREN expr (',' expr)? (',' expr)? RPAREN
    ;

// Lexer Rules
// Keywords
BREAK: 'break';
CONTINUE: 'continue';
WHILE: 'while';
FOR: 'for';
IN: 'in';
RANGE: 'range';

// Arithmetic Operators
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';

// Grouping and Structural Tokens
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
COLON: ':';

// Logical Operators
BOOLEAN: 'True' | 'False';
AND: 'and';
OR: 'or';
NOT: 'not';

// Conditional Keywords
IF: 'if';
ELIF: 'elif';
ELSE: 'else';

// Comparison Operators
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
EQ: '==';
NEQ: '!=';

// Identifiers and Literals
NAME: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER
    : INT
    | FLOAT
    ;
fragment INT: [0-9]+;
fragment FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;
STRING
    : '"' (~["\r\n] | '""')* '"'
    | '\'' (~['\r\n] | '\'\'')* '\''
    ;

// Comments and Whitespace
SINGLE_LINE_COMMENT: '#' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT
    : ('"""' .*? '"""'
    | '\'\'\'' .*? '\'\'\'') -> skip
    ;

// Whitespace Handling
NEWLINE: [\r\n]+ -> skip;
WS: [ \t]+ -> skip;