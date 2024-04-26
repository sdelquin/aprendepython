class File:
    def __init__(self, path: str): ...

    def add_content(self, content: str): ...

    @property
    def size(self):
        sizes = (len(c) for c in self.contents)
        return sum(sizes)

    @property
    def info(self):
        return f'{self.path} [size={self.size}B]'


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple[float], duration: int): ...

    @property
    def info(self): ...


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple[float], duration: int, dimensions: tuple[int]
    ): ...

    @property
    def info(self): ...
