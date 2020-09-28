PSM Validation Tool
===================

The PSM validation tool verifies PSM scans against the ion fragmentation of the associated peptide squence.

Inputs
------

- MZSQLite database generated in a Galaxy workflow
- Tabular file of peptide sequences

By default the tool will fragment peptde into

- b and y ions
- b-H2O, b-NH3, y-H2O, y-NH3
- Internals

You can disable internals and neutral loss ions.

Output
------

A self-contained HTML report that includes:

- All PSMs for peptides of interest with PSM identifiers
- PSM PeptideShaker scores are presented
- MSMS interactive graphs with
    - PSM scan mz and intensities
    - All matching ion fragments
- Ion fragment table 
    - Color coded for matching fragments
    - Internal values and color coded for internal matches