from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJ_ROOT.joinpath('data')


def get_alias_mapping() -> dict[str, str]:
    rename_script = PROJ_ROOT.joinpath('scripts/rename.sh')
    content = rename_script.read_text(encoding='utf8')
    import re

    result = re.findall(
        r'mv +([a-zA-Z0-9]+).fastq.gz +([a-zA-Z0-9]+).fastq.gz', content
    )
    # print(result)

    mapping = dict()
    for k, v in result:
        mapping[v] = k
    return mapping


def DATA(name: str) -> Path:
    mapping = get_alias_mapping()

    if name in mapping.keys():
        name = mapping[name]

    data_path = DATA_DIR.joinpath(name + '.fastq.gz')
    if not data_path.exists():
        raise FileNotFoundError

    return data_path
