import sys


if len(sys.argv) == 1:
    print("Provided string can't be null / has to exist")
    sys.exit(1)

def check_string_validity():
    s = sys.argv[1].strip()
    i = 0
    decimal_counter = 0
    e_counter = 0
    integers = {'0','1','2','3','4','5','6','7','8','9'}
    integer_flag = False

    # Skip first index if it is valid
    if s[0] in {'+', '-'}:
        i +=1
    
    # Handle cases that include '.', 'e' and 'E' as the first char
    if s[0] in {'.', 'e', 'E'}:
        print("False")
        return False

    while i < len(s):
        char = s[i]

        # Check that all chars in the string are valid options
        if char not in integers and char not in {'+', '-', 'e', 'E', '.'}:
            print("False")
            return False

        # Check decimal correctness
        if char == '.':
            decimal_counter += 1
            if decimal_counter >= 2 or e_counter > 0: # Cannot have a '.' after a 'e'
                print("False")
                return False
        
        # Check exponent correctness
        if char in {'e', 'E'}:
            e_counter += 1
            if e_counter >= 2 or not integer_flag: # Either multiple 'e's or no integer before 'e'
                print("False")
                return False
            integer_flag = False # must include an integer after 'e' or 'E'
        
            # If there is an optional sign after e, the sign is skipped in the loop
            if i + 1 < len(s) and s[i + 1] in {'+', '-'}:
                i += 1
        
        # Check that there is no invalid '+' ir '-' (any not after a 'e' or 'E', or right at the start)
        if char in {'+', '-'} and i > 0:
            if s[i - 1] not in {'e', 'E'}:
                print("False")
                return False

        # Check for an integer
        if char in integers:
            integer_flag = True
        i += 1
    
    # Check if an integer was found, and in case of an 'e' or 'E', if there was an integer after
    if not integer_flag:
        print("False")
        return False

    # Finally, return true if number wasn't found to be invalid
    print("True")
    return True



if __name__ == "__main__":
    check_string_validity()
