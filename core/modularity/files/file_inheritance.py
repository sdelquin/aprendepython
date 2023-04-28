class File:
    def __init__(self, path: str):
        self.path = path
        self.contents = []

    def add_content(self, content: str) -> None:
        self.contents.append(content)

    @property
    def size(self) -> int:
        sizes = (len(c) for c in self.contents)
        return sum(sizes)

    @property
    def info(self) -> str:
        return f'{self.path} [size={self.size}B]'


class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple[float], duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self) -> str:
        file_info = super().info
        return f'''{file_info}
Codec: {self.codec}
Geolocalization: {self.geoloc}
Duration: {self.duration}s'''


class VideoFile(MediaFile):
    def __init__(
        self, path: str, codec: str, geoloc: tuple[float], duration: int, dimensions: tuple[int]
    ):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self) -> str:
        media_info = super().info
        return f'''{media_info}
Dimensions: {self.dimensions}'''
