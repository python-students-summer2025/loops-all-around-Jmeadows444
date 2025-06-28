def get_starting_number():
    i = input("How many bottles of beer on the wall? ")
    return int(i)
def sing(start):
    count = start
    while count > 0:
        next_count = count - 1
        print(
            f"{count} bottle{'s' if count != 1 else ''} of beer on the wall, {count} bottle{'s' if count != 1 else ''} of beer.\n"
            f"Take one down and pass it around,"
            f"{next_count if next_count != 0 else 'no more'} bottle{'s' if count - 1 != 1 else ''} of beer on the wall.\n"
        )
        count -= 1 
   