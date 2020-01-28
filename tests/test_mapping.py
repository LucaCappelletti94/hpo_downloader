from typing import Dict
from hpo_downloader import mapping
from tqdm.auto import tqdm
import pandas as pd
import os
from itertools import product
from multiprocessing import Pool, cpu_count


def job(task: Dict):
    month = task["month"]
    cafa4_only = task["cafa4_only"]
    mp_cafa = mapping(month, cafa4_only=cafa4_only)
    if cafa4_only:
        path = f"complete_mapping/{month}_cafa_only.tsv.gz"
    else:
        path = f"complete_mapping/{month}.tsv.gz"
    if not os.path.exists(path):
        mp_cafa.to_csv(path, index=False, sep="\t")
    pd.testing.assert_frame_equal(mp_cafa, pd.read_csv(path, sep="\t"))


def test_all_mapping():
    months = ["october", "november", "december"]
    tasks = [
        {
            "month": month,
            "cafa4_only": cafa4_only
        }
        for month, cafa4_only in product(months, [True, False])
    ]
    os.makedirs("complete_mapping", exist_ok=True)
    with Pool(cpu_count()) as p:
        list(tqdm(p.imap(
            job,
            tasks
        ), total=len(tasks), desc="Rendering mapping"))
