# Class List Manager - Group 11
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Alhaton  (task 3)
def sort_names(names):
    return sorted(names)


# Written by: Alhaton  (task 6)
def to_upper(names):
    return [name.upper() for name in names]


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Upper names:", to_upper(names))


main()

# Written by: Leen (Task 1)
def count_names(names):
    return len(names)

# Add inside main():
    print("Number of names:", count_names(names))
