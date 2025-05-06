def calculate_love_score(name1, name2):
    count1 = count_char(name1.lower() + name2.lower(), "true")
    count2 = count_char(name1.lower() + name2.lower(), "love")
    print(f"{count1}{count2}")


def count_char(name_to_check, word_to_check):
    char_count = 0;
    for x in name_to_check:
        if x in word_to_check:
            char_count += 1
    return char_count
