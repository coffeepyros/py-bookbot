def num_of_words(text):
    word_array = text.split()
    return len(word_array)


def num_of_chars(text):
    stats_dict = {}
    text = text.lower()
    for char in text:
        if char in stats_dict:
            # if value doesnt exist set it to 1
            stats_dict[char] = stats_dict[char] + 1
        else:
            # otherwise increase it by 1
            stats_dict[char] = 1
    return stats_dict
