def stylish_decorator(func):
    def wrapper():
        return f"{'*' * 11}\n{func()}\n{'*' * 11}"
    return wrapper

@stylish_decorator
def greet():
    return "Olá, mundo!"

print(greet())

def greet():
    greetings = ["hello world!"]
    return greetings[0]