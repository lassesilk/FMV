import subprocess


class ExifExtractor:

    def __init__(self, image):
        self.image = image

    def extract_metadata(self):
        info_dict = {}  # Creating the dict to get the metadata tags

        # use Exif tool to get the metadata
        # NB: If you`re doing this on a windows, you have to reference the exifTool.exe in subprocess index 0.
        process = subprocess.Popen(['exifTool', self.image], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)

        # Get the tags in dict
        for tag in process.stdout:
            line = tag.strip().split(':')
            info_dict[line[0].strip()] = line[-1].strip()

        for k, v in info_dict.items():
            print(k, ':', v)
