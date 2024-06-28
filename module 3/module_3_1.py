calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in map(str.lower, list_to_search)

print(string_info("Hello, Python!"))
print(is_contains("python", ["Java", "C++", "Python", "JavaScript"]))
print("Всего вызовов функций:", calls)
