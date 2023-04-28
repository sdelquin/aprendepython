from file_inheritance import VideoFile


def test_core():
    mp4 = VideoFile('/home/python/vanrossum.mp4', 'h264', (23.5454, 31.4343), 487, (1920, 1080))
    mp4.add_content('audio/ogg')
    mp4.add_content('video/webm')
    assert (
        mp4.info
        == '''/home/python/vanrossum.mp4 [size=19B]
Codec: h264
Geolocalization: (23.5454, 31.4343)
Duration: 487s
Dimensions: (1920, 1080)'''
    )
