from hpo_downloader import mapping
from tqdm.auto import tqdm
import pandas as pd
import os


def test_mapping():
    for month in tqdm(
        ("october", "november", "december"),
        desc="Parsing monthly releases"
    ):
        os.makedirs("complete_mapping", exist_ok=True)
        # Testing without cafa filtering
        mp = mapping(month, cafa4_only=False)
        path = f"complete_mapping/{month}.tsv.gz"
        if not os.path.exists(path):
            mp.to_csv(path, index=False, sep="\t")
        pd.testing.assert_frame_equal(mp, pd.read_csv(path, sep="\t"))


def test_cafa_only_mapping():
    for month in tqdm(
        ("october", "november", "december"),
        desc="Parsing monthly releases"
    ):
        os.makedirs("complete_mapping", exist_ok=True)

        # Testing with cafa filtering
        mp_cafa = mapping(month, cafa4_only=True)
        path = f"complete_mapping/{month}_cafa_only.tsv.gz"
        if not os.path.exists(path):
            mp_cafa.to_csv(path, index=False, sep="\t")
        pd.testing.assert_frame_equal(mp_cafa, pd.read_csv(path, sep="\t"))
