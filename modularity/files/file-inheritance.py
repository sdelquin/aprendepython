class File:
    def __init__(self, path):
        self.path = path
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    def size(self):
        sizes = (len(c) for c in self.contents)
        return sum(sizes)

    def info(self):
        return f'{self.path} [size={self.size()}B]'


class MediaFile(File):
    def __init__(self, path, codec, geoloc, duration):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    def info(self):
        file_info = super().info()
        return f'''
{file_info}
Codec: {self.codec}
Geolocalization: {self.geoloc}
Duration: {self.duration}s'''


class VideoFile(MediaFile):
    def __init__(self, path, codec, geoloc, duration, dimensions):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    def info(self):
        media_info = super().info()
        return f'''
{media_info}
Dimensions: {self.dimensions}'''


mp4 = VideoFile('/home/python/vanrossum.mp4', 'h264', (23.5454, 31.4343), 487, (1920, 1080))
mp4.add_content('audio/ogg')
mp4.add_content('video/webm')
print(mp4.info())
