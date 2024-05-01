def markdown_to_blocks(text) -> list[str]:
    return text.split("\2n")[0].split('\n\n')