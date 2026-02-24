# Colors: Red, Green, Yellow, Blue, Magenta, Cyan
print("\033[31mHello, \033[32mthis \033[33mis \033[34mmy \033[35mcolorful \033[36mprogram!")

# Ask for the name
name = input("\033[0mWhat is your name? ")

# Print the final greeting with a mix of colors
print(f"\033[32mNice \033[33mto \033[34mmeet \033[35myou, \033[36m{name}!")

# Reset colors back to normal at the end
print("\033[0m")

