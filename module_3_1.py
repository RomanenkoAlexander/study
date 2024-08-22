calls = 0
def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    fun_result = len(string), string.lower(), string.upper()
    return fun_result

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if item.lower() in string.lower():
            #print("Входит")
            result = True
        else:
            #print("Не входит")
            result = False
        continue
    return result



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)