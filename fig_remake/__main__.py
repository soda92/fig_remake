from fig_remake.download_files import download_file
import sys
from fig_remake.parse_ids import parse_ids

arg0 = sys.argv[1]

if arg0 == "parse":
    parse_ids()

if arg0 == "download":
    download_file("007", "SRR1810907")