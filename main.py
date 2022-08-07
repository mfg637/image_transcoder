import pathlib
import pyimglib
import argparse

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    #argument_parser.add_argument("-i", type=pathlib.Path)
    argument_parser.add_argument("source-images", type=pathlib.Path, nargs="+")
    argument_parser.add_argument("output-directory", type=pathlib.Path)
    args = argument_parser.parse_args()
    outdir: pathlib.Path = getattr(args, 'output-directory')
    image_files: list[pathlib.Path] = getattr(args, 'source-images')
    for image_file in image_files:
        transcoder = pyimglib.transcoding.get_file_transcoder(str(image_file), outdir, image_file.stem, {}, {})
        print(image_file, transcoder)
        transcoder.transcode()


