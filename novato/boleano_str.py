import random
def to_string(value: bool) -> str:
   
    return str(value)
def test_to_string():
    values = [True, False]
    for _ in range(10):
        value = random.choice(values)
        expected = str(value)
        result = to_string(value)
        if result == expected:
            print(f"Input: {value}, Expected: {expected}, Result: {result} - Passed")
        else:
            print(f"Input: {value}, Expected: {expected}, Result: {result} - Failed")

test_to_string()
