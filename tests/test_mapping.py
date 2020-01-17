from hpo_downloader import mapping
from tqdm.auto import tqdm


def test_mapping():
    for month in tqdm(("october", "november", "december")):
        mapping(month, cafa4_only=False).to_csv(
            f"complete_mapping/{month}.tsv",
            index=False,
            sep="\t"
        )
        mapping(month, cafa4_only=True).to_csv(
            f"complete_mapping/{month}_cafa_only.tsv",
            index=False,
            sep="\t"
        )
