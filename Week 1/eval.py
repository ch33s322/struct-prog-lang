def eval(s):
    for c in s:
        assert c in "-0123456789."
    n = 0
    mult = 1.0
    fractional = False
    if s[0] == "-":
        sign = -1
        s = s[1:]
    else:
        sign = 1
    assert len(s) > 0
    assert s != "."
    while len(s) > 0:
        if s[0] == ".":
            assert fractional == False
            fractional = True
        else:
            if not fractional:
                n = n * 10 + ord(s[0]) - ord("0")
            else:
                mult = mult / 10
                n = n + (ord(s[0]) - ord("0") )* mult
                
        s = s[1:]

        
    return n * sign

def test_eval():
    """ test eval """
    print("testing eval")
    assert eval("0") == 0, "expect 0 to be 0"
    assert eval("1") == 1
    assert eval("99") == 99
    assert eval("1890") == 1890
    assert eval("0001") == 1
    assert eval("-99") == -99
    assert eval("1.") == 1
    assert eval("1.0") == 1.0
    assert eval("1.2") == 1.2
    assert eval("-1.2") == -1.2


if __name__ == "__main__":
    test_eval()
    print("done.")