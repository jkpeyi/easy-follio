import re


def extract_title(markdown):
   

    heading_pattern = r'^#\s.*$'


    h1s = re.findall(heading_pattern, markdown, re.MULTILINE)
    if len(h1s) == 0:
        raise Exception("Should have a title")

    else:
        return h1s[0].strip('# ')
