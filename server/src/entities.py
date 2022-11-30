from pydantic import BaseModel


class File(BaseModel):
    """

    File have a filename and data inside it.
    Filename could be any appropriate string.
    Data must be ascii symbols.

    """

    filename: str
    data: str
