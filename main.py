from ExifExtractor import ExifExtractor

exif = ExifExtractor("TestImages/DJI_0002.JPG")
metadata = exif.extract_metadata()

