def get_starting_number():
    return 99

def sing(start):
    count = start
    finished = False
    while not finished:
        if count > 0:
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            count -= 1
            print(f"Take one down and pass it around, {count if count > 0 else 'no more'} bottles of beer on the wall.\n")
        else:
            finished = True
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")