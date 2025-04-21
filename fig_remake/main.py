from fig_remake.download_files import download_file
from fig_remake.parse_ids import parse_ids
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--parse_id",
        "-pa",
        action="store_true",
        default=False,
        help="Parse download id",
    )
    parser.add_argument(
        "--download",
        "-d",
        action="store_true",
        default=False,
        help="download the files",
    )
    args = parser.parse_args()

    if args.parse_id:
        ids = parse_ids()
        for prefix, id in ids:
            print(prefix, id)
    if args.download:
        ids = parse_ids()
        for prefix, id in ids:
            download_file(prefix, id)
