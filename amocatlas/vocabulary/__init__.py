"""amocvocab — the AMOC observing-array variable vocabulary and its tooling.

Contents:

- ``amocvocab.yml`` — the vocabulary (source of truth; hand-edited).
- ``amocvocab.schema.json`` — its JSON Schema.
- ``cf_standard_names.json`` — a committed, pinned subset of the CF standard-name table
  (entry ids + canonical units) that the validator reads, so builds are reproducible.
- ``validate_amocvocab`` — the CI validator.
- ``build_rst`` — generates the docs table.
- ``build_cf_subset`` — regenerates ``cf_standard_names.json`` from the CF table XML.
- ``inventory`` — scans the per-array metadata YAMLs for served variable names.
"""
