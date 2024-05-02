import re
from src.type import BlockType

def block_to_block_type(bloc:str):

    heading_pattern = r'#{1,6}\s(.*)'
    if re.match(heading_pattern, bloc):
        return BlockType.heading
    
    code_block_pattern = r'```([\s\S]*?)```'
    if re.match(code_block_pattern, bloc):
        return BlockType.code
    
    quote_block_pattern = r'^>(.*)$'
    if re.match(quote_block_pattern,bloc, re.MULTILINE):
        return BlockType.quote
    
    unordered_list_pattern = r'^[*-]\s(.*)$'
    if re.match(unordered_list_pattern, bloc,re.MULTILINE):
        return BlockType.ul
    
    ordered_list_pattern = r'^(?:\d+\. )(.*)$'
    if re.match(ordered_list_pattern, bloc,re.MULTILINE):
        return BlockType.ol
    
    return BlockType.paragraph
    
    
    



