"""The start command."""


from json import dumps

from .base import Base


class Start(Base):
    """Start download, preprocess, ingest"""

    def run(self):
        print('Hello, world!')
