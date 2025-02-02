import sys

# Index 1 because index 0 of the list contains the filename
if len(sys.argv) == 1:
    print("Provided string can't be null / has to exist")
    sys.exit(1)

def maximum_sequence_length_check():
    final_count = 0
    temp_counter = 0
    i = 0

    string = sys.argv[1]
    if len(string) == 1:
        print("Maximum sequence length of '()'s in a row found is: 0","\n")
        sys.exit(1)

    while i < len(string) - 1:
        if string[i] == '(' and string[i + 1] == ')':
            temp_counter += 2
            # Skip the next index, since it is a part of a full "()"
            i += 1
        else:
            final_count = max(final_count, temp_counter)
            temp_counter = 0
        # Iterate to next index
        i += 1

    # Handle endcase, where the final pair is the last 2 chars
    final_count = max(final_count, temp_counter)

    print("Maximum sequence length of '()'s in a row found is:", final_count,"\n")
    return final_count

if __name__ == "__main__":
    maximum_sequence_length_check()
