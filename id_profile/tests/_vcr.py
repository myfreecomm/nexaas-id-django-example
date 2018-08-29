from pathlib import Path
from vcr import VCR
from vcr.request import Request

__all__ = ['vcr']


vcr = VCR(
    cassette_library_dir=(Path(__file__).parent / 'fixtures').as_posix(),
)
