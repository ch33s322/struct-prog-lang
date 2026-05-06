import re


#define patterns for tokens
patterns = [
    [r"(\d+)?(\.)?(\d+)", "number"],
    [r"\+", "+"],
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\%", "%"],
    [r"\(", "("],
    [r"\)", ")"],
    [r"\s+", "WHITESPACE"],
    [r".", "error"],
]


for pattern in patterns:
    pattern[0] = re.compile(pattern[0])


def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        assert match
        #process errors
        if tag == "error":
            raise Exception("Syntax error")

        token = {
            "tag":tag,
            "position":position,
            "value":match.group(0)
        }
        if token["tag"] == "number":
            token["value"] = float(token["value"])
        if token["tag"] != "WHITESPACE":
            tokens.append(token)
        position = match.end()

    tokens.append({
        "tag":None,
        "position":position,
        "value":None
    })
    return tokens


def test_simple_token():
    print("test simple token")
    examples = "+-*()"
    for example in examples:
        t = tokenize(example)[0]
        assert t["tag"] == example
        assert t["position"] == 0
        assert t["value"] == example

def test_number_token():
    print("test number tokens")
    for s in ["1", "11", "1.1", "11.1", ".11"]:
        print(s)
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == float(s)


def test_multiple_tokens():
    print("testing multiple tokens")
    tokens = tokenize("1+2")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, {'tag': '+', 'position': 1, 'value': '+'}, {'tag': 'number', 'position': 2, 'value': 2}, {'tag': None, 'position': 3, 'value': None}]
    #print(tokens)


def test_whitespace():
    print("testing white space")
    tokens = tokenize("1 + 2")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1.0}, {'tag': '+', 'position': 2, 'value': '+'}, {'tag': 'number', 'position': 4, 'value': 2.0}, {'tag': None, 'position': 5, 'value': None}]
    #print(tokens)

def test_error():
    print("Test error")
    try:
        t = tokenize("$1+ 2")
        assert False, "should have raised an error"
    except Exception as e:
        assert "Syntax error" in str(e), f"Unexpected Exception: {e}"


def test_modulus():
    print("testing modulus")
    tokens = tokenize("10 % 3")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 10.0}, {'tag': '%', 'position': 3, 'value': '%'}, {'tag': 'number', 'position': 5, 'value': 3.0}, {'tag': None, 'position': 6, 'value': None}]


if __name__ == "__main__":
    test_simple_token()
    test_number_token()
    test_multiple_tokens()
    test_whitespace()
    test_error()
    test_modulus()
    