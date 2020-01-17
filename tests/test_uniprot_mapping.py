from hpo_downloader import uniprot_mapping
import pytest


def test_uniprot_mapping():
    for month in ("october", "november", "december"):
        uniprot_mapping(month)
    with pytest.raises(ValueError):
        uniprot_mapping("kebab")
