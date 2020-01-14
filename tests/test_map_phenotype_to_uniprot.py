from hpo_downloader import map_phenotype_to_uniprot


def test_map_phenotype_to_uniprot():
    phenotype_to_uniprot = map_phenotype_to_uniprot()
    phenotype_to_uniprot.to_csv(
        "phenotype_to_uniprot.tab", sep="\t", index=False)
    phenotype_to_uniprot = map_phenotype_to_uniprot(cafa4_only=True)
    phenotype_to_uniprot.to_csv(
        "phenotype_to_uniprot_cafa4_only.tab", sep="\t", index=False)
