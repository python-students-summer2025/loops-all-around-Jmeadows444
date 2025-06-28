def get_starting_number():
    i = input("How many bottles of beer on the wall? ")
    return int(i)

def sing(start):
    for i in range(start, 0, -1):
        bottle_word = "bottle" if i == 1 else "bottles"
        next_bottles_word = "bottle" if i - 1 == 1 else "bottles"
        next_count = f"{i - 1}" if i - 1 > 0 else "no more"

        print(f"{i} {bottle_word} of beer on the wall, {i} {bottle_word} if beer.")
        print(f"Take one down, pass it around, {next_count} {next_bottles_word} of beer on the wall.\n")
