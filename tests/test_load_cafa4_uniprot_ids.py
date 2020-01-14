from hpo_downloader import load_cafa4_uniprot_ids


def test_load_cafa4_uniprot_ids():
    load_cafa4_uniprot_ids().to_csv("cafa.csv", index=False)
