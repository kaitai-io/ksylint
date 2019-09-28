<h1 align="center">ksylint</h1>

<p align="center">Check kaitai .ksy files for errors and style flaws.</p>

<p  align="center">
 <a href="https://dev.azure.com/cugu/dfir/_build?definitionId=5&_a=summary"><img src="https://img.shields.io/azure-devops/build/cugu/dfir/5" alt="build" /></a>
 <a href="https://dev.azure.com/cugu/dfir/_build?definitionId=5&_a=summary"><img src="https://img.shields.io/azure-devops/coverage/cugu/dfir/5" alt="coverage" /></a>
</p>

## Installation

``` bash
# pip install ksylint TODO
```

## Usage
``` bash
# ksylint hello_world.ksy TODO
```

### Missing style guide tests
1. General formatting
    - Use block YAML style in most general cases, unless explicitly specified/allowed otherwise.
    - Formatting of maps-inside-sequences MUST have - delimiter and first map element on the same first line, i.e.:
2. Order of sections in a type spec
    - all
3. Meta section (meta)
    - all
4. Documentation
    - all
5. Sequence attributes
    - all
6. Instance attributes
    - all
7. Transcribing existing specs
    - all

### Not checked
- All identifiers, docstrings, comments and generally all human-readable text SHOULD be kept in English, unless there’s a very good reason not to do so.
