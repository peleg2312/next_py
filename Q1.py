# מדפיסה את השם הארוך ביותר בקובץ
def print_longest_name(filename):
    print(max(open(filename).read().splitlines(), key=len))

# מדפיסה את סך אורכי כל השמות בקובץ
def print_total_length(filename):
    print(sum(len(name) for name in open(filename).read().splitlines()))

# מדפיסה את השמות הקצרים ביותר בקובץ
def print_shortest_names(filename):
    names = open(filename).read().splitlines()
    min_length = min(len(name) for name in names)
    print("\n".join(name for name in names if len(name) == min_length))

# מכניסה לקובץ היעד את אורכי השמות בקובץ הקלט
def create_name_length_file(input_filename, output_filename):
    with open(output_filename, 'w') as f:
        f.write("\n".join(str(len(name)) for name in open(input_filename).read().splitlines()))

# מדפיסה את השמות בקובץ שיש להם אורך מסוים
def print_names_of_length(filename, length):
    print("\n".join(name for name in open(filename).read().splitlines() if len(name) == length))

def main():
    filename = "names.txt"  # עדכן את שם הקובץ
    output_filename = "name_lengths.txt"  # עדכן את שם קובץ הפלט
    length_to_find = 4  # עדכן את אורך השמות לחיפוש

    print_longest_name(filename)
    print_total_length(filename)
    print_shortest_names(filename)
    create_name_length_file(filename, output_filename)
    print_names_of_length(filename, length_to_find)

main()