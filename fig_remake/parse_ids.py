from pathlib import Path
import re
from typing import List


def parse_ids(sh_file: Path) -> List[List[str]]:
    ret = []

    c = sh_file.read_text(encoding="utf8")
    for line in c.split("\n"):
        if line.strip() == "":
            continue
        _, prefix, id = re.findall(
            r"fastq/([a-zA-Z0-9]+)/([0-9]+)/([a-zA-Z0-9]+)", line
        )[0]
        # print(srr, prefix, id)
        ret.append([prefix, id])
    return ret
