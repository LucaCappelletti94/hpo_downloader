hpo_downloader
===========================================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package to download `HPO annotations <https://hpo.jax.org/app/download/annotation>`__
and mapping to `Uniprot ID and AC <https://www.uniprot.org/>`__
and `CAFA4 IDs <https://www.biofunctionprediction.org/cafa/>`__.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install hpo_downloader


Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get
slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Pipeline
----------------------------------------------
The package pipeline is illustrated in the following image:

|pipeline|


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/hpo_downloader.png
   :target: https://travis-ci.org/LucaCappelletti94/hpo_downloader
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_hpo_downloader&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_hpo_downloader
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_hpo_downloader&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_hpo_downloader
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_hpo_downloader&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_hpo_downloader
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/hpo_downloader/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/hpo_downloader?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/hpo-downloader.svg
    :target: https://badge.fury.io/py/hpo-downloader
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/hpo-downloader
    :target: https://pepy.tech/badge/hpo-downloader
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/26d152932db342a09ac6b009889255c9
    :target: https://www.codacy.com/manual/LucaCappelletti94/hpo_downloader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/hpo_downloader&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |pipeline|  image:: https://github.com/LucaCappelletti94/hpo_downloader/blob/master/HPO%20downloader.png?raw=true
    :alt: Pipeline

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/0cac3687d5c9520e561a/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/hpo_downloader/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/0cac3687d5c9520e561a/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/hpo_downloader/test_coverage
    :alt: Code Climate Coverate