from tokenizer import *
from parser import *

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    if ast["tag"] in ["+", "-", "*", "/"]:
        left = evaluate(ast["left"])
        right = evaluate(ast["right"])
        if ast["tag"] == "+":
            return left + right
        if ast["tag"] == "-":
            return left - right
        if ast["tag"] == "*":
            return left * right
        if ast["tag"] == "/":
            return left / right


def test_evaluate_number():
    print("test eval number")
    assert evaluate({"tag":"number", "value":4}) == 4


def test_evaluate_addition():
    print("test evaluate addition")
    ast = {"tag":"+", "value":"+", "left":{"tag":"number", "value":3}, "right":{"tag":"number", "value":1}}
    assert evaluate(ast) == 4

def test_evaluate_subtraction():
    print("test evaluate subtraction")
    ast = {"tag":"-", "value":"-", "left":{"tag":"number", "value":3}, "right":{"tag":"number", "value":1}}
    assert evaluate(ast) == 2

def test_evaluate_multiplication():
    print("test evaluate multiplication")
    ast = {"tag":"*", "value":"*", "left":{"tag":"number", "value":3}, "right":{"tag":"number", "value":2}}
    assert evaluate(ast) == 6

def test_evaluate_division():
    print("test evaluate division")
    ast = {"tag":"/", "value":"/", "left":{"tag":"number", "value":4}, "right":{"tag":"number", "value":2}}
    assert evaluate(ast) == 2

def test_evaluate_expression():
    assert eval("1+2+3") == 6
    assert eval("1+2*3") == 7
    assert eval("1-2+3") == 2
    assert eval("(1+2)*3") == 9


def parse(tokens):
    ast, tokens = parse_expression(tokens)
    return ast

def eval("s"):
    tokens = tokenize(s)
    ast = parse(tokens)
    result = evaluate(ast)
    return result


if __name__ == "__main__":
    test_evaluate_number()
    test_evaluate_addition()
    test_evaluate_subtraction()
    test_evaluate_multiplication()
    test_evaluate_division()
    test_evaluate_expression()
    print("done.")