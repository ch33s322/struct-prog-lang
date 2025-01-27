



simple_expression = number | identifier | "(" expression ")" | "-" simple_expression
factor = simple_expression
term = factor { "*"|"/" factor }
arithmetic_expression = term { "+"|"-" term }
comparison_expression == arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">="  arithmetic expression ]
boolean_term == comparison_expression { "&&" comparison_expression }
boolean_expression == boolean_term { "||" boolean_term }
expression = boolean_expression
print_statement = "print" "(" expression ")"
assignment_statement = expression
statement = print_statement |
assignment_expression
statement_list = statement { ";" statement } {";"}
program = statement_list
