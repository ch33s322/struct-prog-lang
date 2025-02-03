from tokenizer import *



"""
factor = <number> | "(" expression ")"
term = factor { "*"|"/" factor }
arithmetic_expression = term { "+"|"-" term }
"""




def parse_factor(tokens):
    token = tokens[0]
    if token["tag"] == "number":
        return {
            "tag":"number",
            "value":token["value"]
        }, tokens[1:]
    if token["tag"] == "(":
        tokens = tokens[1:]
        ast, tokens = parse_expression(tokens)
        print(tokens)
        #assert tokens[0]["tag"] == ")"
        return ast, tokens[1:]
    raise Exception(f"Unexpected token '{token['tag']}' at position {token['position']} ")


def parse_term(tokens):
    node, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        tag = tokens[0]["tag"]
        tokens = tokens[1:]
        rhs, tokens = parse_factor(tokens)
        node = {"tag":tag, "left":node, "right":rhs}
    return node, tokens

def parse_expression(tokens):
    node, tokens = parse_term(tokens)
    while tokens[0]["tag"] in ["+", "-"]:
        tag = tokens[0]["tag"]
        tokens = tokens[1:]
        rhs, tokens = parse_term(tokens)
        node = {"tag":tag, "left":node, "right":rhs}
    return node, tokens


def test_parse_factor():
    print("test parse factor")
    for s in ["1", "23", "333", "(560)"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        print(ast)
        print(tokens)

        
def test_parse_term():
    print("test parse term")
    for s in ["15", "233", "333111"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        print(ast)
        print(tokens)

def test_parse_expression():
    print("test parse expression")
    for s in ["15", "233", "3*33+111"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        print(ast)
        print(tokens)

if __name__ == "__main__":
    test_parse_factor()
    test_parse_term()
    test_parse_expression()