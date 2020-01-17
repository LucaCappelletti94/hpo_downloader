import pandas as pd
from ..utils import load_columns


def hpo_annotations() -> pd.DataFrame:
    """Return dataframe containing phenotype HPO annotations."""
    df = pd.read_csv(
        "http://compbio.charite.de/jenkins/job/hpo.annotations/lastStableBuild/artifact/misc/phenotype_annotation.tab",
        sep="\t"
    )
    df.columns = load_columns()
    return df
