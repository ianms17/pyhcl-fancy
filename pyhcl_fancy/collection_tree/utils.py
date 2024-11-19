import pathlib


def _is_directory(file_path: str) -> bool:
    return  pathlib.Path(file_path).is_dir()