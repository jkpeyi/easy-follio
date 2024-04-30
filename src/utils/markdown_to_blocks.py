def markdown_to_blocks(text):
    return text.split("\2n")[0].split('\n\n')