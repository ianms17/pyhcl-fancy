import pathlib
import hcl2


def _open_all_tf_files(directory_path: str) -> dict:
    tf_dir = pathlib.Path(directory_path)
    tf_file_content = {}
    
    for tf_file in tf_dir.rglob("/*.tf"):
        with open(tf_file, "r") as f:
            tf_file_content[tf_file] = hcl2.load(f)
    
    return tf_file_content