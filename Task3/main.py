import sys


if len(sys.argv) == 1:
    print("Provided list can't be null / has to exist")
    sys.exit(1)

def calculate_largest_rectangle():
    height_data = []
    stack = []
    max_area = 0
    index = 0

    while index < len(sys.argv) - 1:
        # Convert the str variables provided to int and strip away all non-numbers (index + 1 because sys.argv index [0] contains "main.py")
        height_data.append(int(sys.argv[index + 1].strip("[],")))
        index += 1
    
    length = len(height_data)

    # Go through all y-values at every x position
    for i in range(length):
        # If the current y-value at x is lower than the y-value at top of the stack, calculate the area
        while stack and height_data[i] < height_data[stack[-1]]:
            # Get the height of the y-coordinate
            height = height_data[stack.pop()]

            # Calculate the width of x
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            
            # max_area gets updated in case a bigger rectangle was found
            max_area = max(max_area, height * width)

        # The current y-coordinate index gets appended to the stack
        stack.append(i)

    # Calculate area for remaining y-coordinates in the stack
    while stack:
        height = height_data[stack.pop()]
        if not stack:
            width = length
        else:
            width = length - stack[-1] - 1
        
        max_area = max(max_area, height * width)

    print(max_area)
    return max_area

if __name__ == "__main__":
    calculate_largest_rectangle()
