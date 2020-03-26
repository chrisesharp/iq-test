def iq_test(string_of_numbers):
    odds = [int(x)%2!=0 for x in string_of_numbers.split()]
    return odds.index(True) + 1 if odds.count(True) == 1 else odds.index(False) + 1