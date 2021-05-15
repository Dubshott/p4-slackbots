#------------------------------------------------------------------------------------------------------------------
# This section from lines 1 - 30 are the things we use in different segments of code

#creating the class 'BubbleSort'
class bubbleSort:
    def init(self):
        # Creating a loop where we start with the length of 'self' minus 1, and we go to 0 with increments of -1
        for i in range(len(self) - 1, 0, -1):
            # Creating another loop with j and continue it until i stops
            for j in range(i):
                # The computer checks if the first value is greater than the value after it
                if self[j] > self[j + 1]:
                    # If it is, we store the bigger value (self[j]) and store into a temporary variable, temp
                    temp = self[j]
                    # Then we store the smaller value (self[j+1]) into self[j]
                    self[j] = self[j + 1]
                    # Once that happens, we put the temporary variable into the self[j+1]
                    self[j + 1] = temp
            # This piece of code allows us to see the different iterations and how the computer is slowly sorting...
            # ...through the different numbers.
            # It is necessary to keep this here, because it needs to use the i values in the for i in range loop
            print(f'Iteration: {abs(i - len(self))}', self)
# In the end this class is able to swap the values in the list to make sure the numbers are ordered.

# In this section of code I am creating a dictionary which tells the number value of each letter
letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12,
           "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24,
           "y":35, "z":26}

#------------------------------------------------------------------------------------------------------------------

# The first part of our code (lines 32 - 47) is to bubble sort some numbers that we set beforehand
print("Part 1: BubbleSort with List\n")
# Right here, we have the list that the computer will be sorting (basically #s between 10 to 90)
list_to_sort = [90, 50, 10, 20, 70, 60, 40, 30, 80]
# We first print out our original list, just so people can see
print('Original List: ', list_to_sort)
# Then, we use our class BubbleSort and sort through the list that we defined above
# While this is going on, the print in the class is printing out all the iterations and showing how the...
# ...computer is sorting everything out
bubbleSort.init(list_to_sort)
# Finally, we print out the sorted list
print('Sorted List: ', list_to_sort)

# This section of code allowed us to bubble sort through a list that we defined earlier.

#------------------------------------------------------------------------------------------------------------------
print("\n")
# This second part of our code (lines 49 - 77) is to bubble sort numbers that the user chooses
print("Part 2: BubbleSort with User Input List\n")
# First we get the user input so we know what numbers we need to sort
example_string = input("Please enter a string of numbers (Make sure you separate the numbers with commas!): ")
# Once we do that we create a list out of the numbers we got, but we change them into numbers instead of letters
# We also put commas in between each number
int_list = list(map(int, example_string.split(",")))

# First, we are creating a new list called list0. Then we append the values from our int_list into this string
# From there, we just print out that list to show the viewer our original list
listO = []
listO.append(int_list)
print("OriginalList")
print(listO)

# Now, we start the bubble sorting by switching back to our class. We start the initialization with int_list
# This will go through our entire Bubble Sorting process from the class above and will completely sort the list
# This will keep the sorted list within int_list
bubbleSort.init(int_list)

# Now we create another list called 'listS' and we append our int_list now, since the int_list is the sorted list
listS = []
listS.append(int_list)
print("Sorted List")
print(listS)

# This section of code allowed us to take some user input and sort those different integers.

#------------------------------------------------------------------------------------------------------------------
print("\n")
# This third of our code (lines )bubble sorts through different letters instead of numbers.
# It numbers all the letters according to the letters' position in the alphabet
# We use the dictionary that we defined above to swap the letters into numbers that we can easily sort
print("Part 3: BubbleSort with User Input with Alphabet\n")
# First, we are taking 5 letters that the user can choose
letter1 = input("Please input your 1st letter: ")
letter2 = input("Please input your 2nd letter: ")
letter3 = input("Please input your 3rd letter: ")
letter4 = input("Please input your 4th letter: ")
letter5 = input("Please input your 5th letter: ")
print("\nAwesome! You said,", letter1, letter2, letter3, letter4, letter5, ". In the alphabet these are numbered,", letters[letter1], letters[letter2], letters[letter3], letters[letter4], letters[letter5], ",respectively.")

sort_letter_list = [letter1, letter2, letter3, letter4, letter5]
print('Original List: ', sort_letter_list)
bubbleSort.init(sort_letter_list)
print('Sorted List: ', sort_letter_list)

# This section of code allowed us to get the user input again but sort through the letters of the alphabet

#------------------------------------------------------------------------------------------------------------------#

