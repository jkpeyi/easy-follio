from src.utils import block_to_block_type, markdown_to_blocks
from src.parentnode import ParentNode
from src.types import BlockType
from src.blocs import *


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)

    div = ParentNode("div", [__cast(block) for block in blocks])

    return div


def __cast(block):

    obj = {
        BlockType.code: Code(block),
        BlockType.heading: Heading(block),
        BlockType.ol: Ol(block),
        BlockType.ul: Ul(block),
        BlockType.paragraph: Paragraph(block),
        BlockType.quote: Quote(block),
    }

    return obj[block_to_block_type(block)]
