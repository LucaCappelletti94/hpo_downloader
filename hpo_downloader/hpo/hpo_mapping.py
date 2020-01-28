import pandas as pd


def hpo_mapping() -> pd.DataFrame:
    """Return dataframe containing phenotype HPO mapping."""
    df = pd.read_csv(
        "http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/lastSuccessfulBuild/artifact/annotation/ALL_SOURCES_ALL_FREQUENCIES_phenotype_to_genes.txt",
        sep="\t"
    )
    columns = df.columns[0].split(": ")[-1].split("<tab>")
    df = df.reset_index()
    df.columns = columns
    df = df.drop(columns=[
        "Gene-Name",
        "HPO-Name"
    ])
    df = df.rename(columns={
        "Gene-ID": "gene_id",
        "HPO-ID": "hpo_id"
    })
    return df
