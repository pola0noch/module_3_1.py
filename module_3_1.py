calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains(string, list_to_search):
    count_calls()
    new_list_to_search = [s.lower() for s in list_to_search]
    return new_list_to_search.__contains__(string.lower())

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)