def cut_long_line(line, max_length, cut_indicator, indent_chars, align_chars=None):
    """
    Cut a long line into multiple lines of specified maximum length, while preserving indentation
    and aligning the continuation lines on the first occurrence of one of the specified alignment characters.
    
    :param line: str, the line to be cut
    :param max_length: int, the maximum length of each line after cutting
    :param cut_indicator: str, the character or string to indicate a cut in the line
    :param indent_chars: list, the characters considered as indentation characters
    :param align_chars: list, the characters to align the continuation lines, None or an empty list for no alignment
    :return: str, the cut line as a single string with line breaks
    """
    # Check if the line is already short enough
    if len(line) <= max_length:
        return line
    
    # Extract the indentation from the input line
    indent = ''
    for char in line:
        if char in indent_chars:
            indent += char
        else:
            break

    if align_chars:
        # Find the alignment index by checking the first occurrence of any alignment character
        align_index = len(line)
        for char in align_chars:
            char_index = line.find(char)
            if char_index != -1:
                align_index = min(align_index, char_index + 1)
    else:
        align_index = 0

    # Initialize the cut_line variable
    cut_line = ''

    # Limite le nombre de coupures à 10
    nb_max_coupures = 10
    nb_coupures = 0
    
    if len(indent) == 0 and align_index == 0:
        indent = "  "
        

    # Cut the line into segments of max_length or less, and align the continuation lines if needed
    while len(line) > max_length and nb_coupures < nb_max_coupures:
        # Find the last space character within the max_length limit
        cut_index = line.rfind(' ', 0, max_length)

        # Add the segment up to the cut_index to the cut_line and include the cut_indicator
        cut_line += line[:cut_index] + cut_indicator + '\n'

        # Update the line variable by removing the processed segment and adding the indentation and alignment (if any)
        line = indent + ' ' * align_index + line[cut_index + 1:]
        # print("align_index = ", align_index, "max_length = ", max_length, "cut_index = ", cut_index, "indent = '", repr(indent), "' " , "line = '", line, "'")
        nb_coupures += 1
    cut_line += line

    return cut_line


