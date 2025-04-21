from fig_remake.download_files import download_file
import sys
from fig_remake.parse_ids import parse_ids

def main():
    arg0 = sys.argv[1]

    if arg0 == "parse":
        parse_ids()

    if arg0 == "download":
        ids = parse_ids()
        ids0 = ids[0]
        download_file(ids0[0], ids0[1])
