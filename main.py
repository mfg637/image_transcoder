import pathlib
import pyimglib
import argparse
import config
import logging

logging.basicConfig(
    format="%(process)dx%(thread)d::%(levelname)s::%(name)s::%(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("source-images", type=pathlib.Path, nargs="+")
    argument_parser.add_argument("output-directory", type=pathlib.Path)
    argument_parser.add_argument("--force-audio-transcode", action="store_true")
    argument_parser.add_argument("--cpu-used", type=int, default=None)
    args = argument_parser.parse_args()
    outdir: pathlib.Path = getattr(args, 'output-directory')
    image_files: list[pathlib.Path] = getattr(args, 'source-images')
    if args.cpu_used is not None:
        pyimglib.config.aomenc_cpu_usage = args.cpu_used
    pyimglib.config.force_audio_transcode = args.force_audio_transcode
    for image_file in image_files:
        transcoder = pyimglib.transcoding.get_file_transcoder(image_file, outdir, image_file.stem)
        result = transcoder.transcode()
        pyimglib.transcoding.statistics.update_stats([result])
    pyimglib.transcoding.statistics.log_stats()


