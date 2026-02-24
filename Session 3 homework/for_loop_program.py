# # --- User Input Section ---
# # We use input() to wait for your command
# shape_choice = input("What pattern? (triangle, square, pyramid): ").lower()
# char = input("What character should I use? (e.g. *, #): ")

# # Safety net: This prevents the 'ValueError' you just saw
# try:
#     size = int(input("How big should it be? (Enter a number): "))
# except ValueError:
#     print("Error: Please enter a whole number for the size!")
#     exit() # Stops the script if the input isn't a number

# print(f"\n--- Printing {shape_choice} ---\n")

# # --- Pattern Logic ---

# # 1. Right-Angled Triangle
# if shape_choice == "triangle":
#     for i in range(1, size + 1):
#         for j in range(i):
#             print(char, end="")
#         print()

# # 2. Square Pattern
# elif shape_choice == "square":
#     for i in range(size):
#         for j in range(size):
#             print(char, end=" ")
#         print()

# # 3. Pyramid Pattern
# elif shape_choice == "pyramid":
#     for i in range(1, size + 1):
#         # Handle the left-side padding
#         for j in range(size - i):
#             print(" ", end="")
#         # Handle the symbols
#         for k in range(2 * i - 1):
#             print(char, end="")
#         print()

# else:
#     print("Shape not recognized. Please run again and choose triangle, square, or pyramid.")

# I was combining both of the loops.
# The 'while' loop keeps the whole program alive
running = True

print("--- Welcome to the Pattern Machine ---")

while running:
    print("\nOptions: 1. Square | 2. Triangle | 3. Exit")
    choice = input("What would you like to do? ")

    if choice == "3":
        print("Goodbye!")
        running = False  # This 'breaks' the while loop
    
    elif choice == "1" or choice == "2":
        char = input("Enter a character (e.g., *): ")
        size = int(input("Enter size: "))

        # The 'for' loops are nested inside the 'while' loop
        if choice == "1":
            print("\nDrawing Square:")
            for i in range(size):
                for j in range(size):
                    print(char, end=" ")
                print()
        
        elif choice == "2":
            print("\nDrawing Triangle:")
            for i in range(1, size + 1):
                for j in range(i):
                    print(char, end="")
                print()
    else:
        print("Invalid choice, try again.")

# I use this for patterns because I have a defined count.
# I know the start and the end before the loop even begins.
# I combined while and for to show how they can work together despite for could be used alone here.