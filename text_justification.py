def textJustification(words, l):
    def break_up_sentences(arr, l):
        sentences = []
        current_words = []
        current_count = 0

        for word in words:
            if current_count + len(word) + len(current_words) <= l:
                current_count += len(word)
                current_words.append(word)

            else:
                sentences.append(current_words)
                current_words = [word]
                current_count = 1
        
        if current_words:
            sentences.append(current_words)

        return sentences

    def calculate_spaces(arr, l):
        sentence_length = 0
        for word in arr:
            sentence_length += len(word)
        spaces = l - sentence_length
        return spaces

    def add_spaces(arr, number_of_spaces):
        words_in_arr = len(arr)
        if words_in_arr == 2:
            spaces_to_insert = [" "] * number_of_spaces
            spaces = "".join(spaces_to_insert)
            arr.insert(1, spaces)
        elif words_in_arr == 3:
            if number_of_spaces % 2 == 0:
                spaces_to_insert = [" "] * (number_of_spaces // 2)
                spaces = "".join(spaces_to_insert)
                arr.insert(1, spaces)
                arr.insert(2, spaces)
            else:
                right_total = number_of_spaces // 2
                left_total = number_of_spaces - right_total
                right_spaces = [" "] * (right_total)
                right = "".join(right_spaces)
                left_spaces = [" "] * (left_total)
                left = "".join(left_spaces)
                arr.insert(1, left)
                arr.insert(3, right)

        elif words_in_arr == 1:
            spaces_to_insert = [" "] * number_of_spaces
            spaces = "".join(spaces_to_insert)
            arr.append(spaces)

        return arr

    answer = []

    sentence_arr = break_up_sentences(words,l)
    for sentence in sentence_arr:
        number_of_spaces = calculate_spaces(sentence, l)
        sentence_with_spaces = add_spaces(sentence, number_of_spaces)
        answer.append("".join(sentence_with_spaces))

    return answer