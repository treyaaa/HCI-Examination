def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Starting position: (0, 0)")
    print("Enter directions (N, S, E, W) or type STOP to end.")

    while True:
        move = input("Enter direction: ").strip().lower()

        if move == "stop":
            break
        elif move in ["n", "north"]:
            y += 1
        elif move in ["s", "south"]:
            y -= 1
        elif move in ["e", "east"]:
            x += 1
        elif move in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input! Please enter N, S, E, W, or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    # Final result
    print(f"\nFinal position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin (0, 0).")


# Run the program
gps_tracker()
