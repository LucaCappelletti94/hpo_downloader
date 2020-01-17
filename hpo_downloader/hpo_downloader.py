import pandas as pd
from .utils import load_urls, format_uniprot_mapping_request, load_columns, load_paths
from typing import List
import urllib
import warnings
from encodeproject import download
import shutil
import os
from tqdm.auto import tqdm


def map_phenotype_to_uniprot(
    cafa4_only: bool = False
) -> pd.DataFrame:
    """Return dataframe containing mapping from phenotype to uniprot.

    Parameters
    --------------------------
    cafa4_only: bool = False,
        Whetever to return only mapping whose uniprot ID is contained in CAFA4 annotations.
    """
    hpo = map_geneid_to_phenotype()
    uniprot = map_geneid_to_uniprot(hpo["entrez-gene-id"].unique())
    mapping = {}
    if cafa4_only:
        uniprot_ids = load_cafa4_uniprot_ids()["Uniprot_Id"].unique()
    for gene_id, group in tqdm(uniprot.groupby("entrez-gene-id"), desc="Mapping Uniprot Ids to phenotypes"):
        for uniprot_id in group["Uniprot_ID"]:
            if not cafa4_only or uniprot_id in uniprot_ids:
                mapping[uniprot_id] = mapping.get(uniprot_id, []) + [
                    hpo_id
                    for hpo_id in hpo[hpo["entrez-gene-id"] == gene_id]["HPO-Term-ID"].values
                ]

    if cafa4_only:
        unmapped_genes = set(uniprot_ids) - set(mapping.keys())
        if unmapped_genes:
            warnings.warn("Unable to map {number} ({percentage:.2%}) CAFA4 uniprot ids to HPO phenotypes!".format(
                number=len(unmapped_genes),
                percentage=len(unmapped_genes)/len(uniprot_ids)
            ))

    return pd.DataFrame(
        [
            (key, value)
            for key, values in mapping.items()
            for value in values
        ],
        columns=[
            "Uniprot_ID",
            "HPO-Term-ID"
        ]
    )
