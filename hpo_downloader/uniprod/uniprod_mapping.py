import pandas as pd
import os


def _path(month: str, filename: str):
    return "{pwd}/../../uniprod_mapping/{month}/{filename}.tsv.gz".format(
        pwd=os.path.dirname(os.path.abspath(__file__)),
        month=month,
        filename=filename
    )


def uniprod_gene_id_mapping(month: str) -> pd.DataFrame:
    """Return DataFrame containing the mapping between uniprod AC and GeneId.

    Parameters
    ----------------------
    month:str
        The month whose mapping to be loaded.

    Returns
    ----------------------
    The Dataframe containing the mapping between uniprod AC and GeneId.
    """
    return pd.read_csv(
        _path(month, "geneid"),
        sep="\t"
    )


def uniprod_human_mapping(month: str) -> pd.DataFrame:
    """Return DataFrame containing the mapping between uniprod AC and human uniprod ID.

    Parameters
    ----------------------
    month:str
        The month whose mapping to be loaded.

    Returns
    ----------------------
    The Dataframe containing the mapping between uniprod AC and human uniprod ID
    """
    return pd.read_csv(
        _path(month, "human"),
        sep="\t"
    )
