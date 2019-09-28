# kaitai linter

Check kaitai .ksy files for errors and style flaws

## TODO

Not implemented yet:
1. Missing
    - Block YAML style in most general cases, unless explicitly specified/allowed otherwise.
    - Formatting of maps-inside-sequences MUST have - delimiter and first map element on the same first line, i.e.:
2. Order of sections in a type spec
3. Meta section (meta)
4. Documentation
5. Sequence attributes
6. Instance attributes
7. Transcribing existing specs

Not checked:
- All identifiers, docstrings, comments and generally all human-readable text SHOULD be kept in English, unless there’s a very good reason not to do so.
