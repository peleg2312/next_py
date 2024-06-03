from animals import IDIterator


def check_id_valid(id_number):
    id_str = str(id_number)
    if len(id_str) != 9 or not id_str.isdigit():
        return False

    multiplied_digits = [int(digit) * (1 if i % 2 == 0 else 2) for i, digit in enumerate(id_str)]

    processed_digits = [digit if digit < 10 else digit - 9 for digit in multiplied_digits]

    total_sum = sum(processed_digits)

    return total_sum % 10 == 0
    # בודק האם תעודת הזהות תקינה לפי התנאים של המשימה


def id_generator(start_id):
    current_id = start_id
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1
    # יצירת גנרטור שמייצר תעודות זהות תקינות החל מתעודת הזהות ההתחלתית


def main():
    id_number = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")

    if choice == "it":
        id_iter = IDIterator(id_number)
        for _ in range(10):
            try:
                print(next(id_iter))
            except StopIteration:
                print("No more valid IDs")
                break
    elif choice == "gen":
        id_gen = id_generator(id_number)
        for _ in range(10):
            try:
                print(next(id_gen))
            except StopIteration:
                print("No more valid IDs")
                break
    else:
        print("Invalid choice")
    # לפי הקלט שנקלט (gen or it) מפעיל את הפעולה הרצויה ומחזיר את 10 תעודות הזהות הבאות התקינות אחרי הת"ז שנקלטה (לא כולל)

if __name__ == "__main__":
    main()
