def sorter(list_1, list_2, reverse=False):
    """
    Sorts list_1 and list_2 based on list_2's values;
    Useful for processing data before plotting them.

    list_1 and list_2 must be of equal length.

    Parameters
    ----------
    list_1 : list
    list_2 : list
        list to sort by
        note that both will be sorted

    reverse : bool
        if True descending
        if False ascending

    Returns
    -------
    tuple
        (list_1_sorted, list_2_sorted) both sorted by list_2

    """
    lists = [(l1, l2) for l1, l2 in zip(list_1, list_2)]
    lists.sort(reverse=reverse, key=lambda x: x[1])
    list_1_sorted = [item[0] for item in lists]
    list_2_sorted = [item[1] for item in lists]

    return (list_1_sorted, list_2_sorted)


def clean(text):
    """
    Cleans the content of text by stripping leading and trailing
    whitespace, removing punctuation, and rendering all letters lowercase.

    Parameter
    ----------
    text : str

    Returns
    -------
    str
        cleaned content of the text
    """
    puncts = string.punctuation + "‘’“”"

    # Stripping leading and trailing whitespace:
    text = text.strip()

    # Cleaning punctuation
    text = text.replace('.', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans('', '', puncts))
    text = text.replace('\x92', "'")
    return text.lower()


def ngrams(text, n=1):
    """
    Counts the number of times a contiguous sequence of n words appeared
    in the text.

    Parameters
    ----------
    text : str
        text to find ngrams in
    n : int, optional (default 1)
        value of -grams

    Returns
    -------
    sorted_grams : dictionary
        ngram string as keys and their counts as values
    """
    grams_list = []
    grams_dict = {}
    list_of_paragraphs = text.split('\n')

    for paragraph in list_of_paragraphs:
        words = paragraph.split()
        for index in range(0, len(words)):
            temp = words[index:index+n]
            if len(temp) == n:
                grams_list.append(' '.join(word for word in
                                           words[index:index+n]))
    for term in grams_list:
        if term not in grams_dict:
            grams_dict[term] = 1
        else:
            grams_dict[term] += 1

    sorted_grams = dict(sorted(grams_dict.items(),
                               key=lambda temp: (-temp[1], temp[0])))
    return sorted_grams