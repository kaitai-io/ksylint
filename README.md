<h1 align="center">ksylint</h1>

<p align="center">Check kaitai .ksy files for errors and style flaws.</p>

<p  align="center">
 <a href="https://dev.azure.com/cugu/dfir/_build?definitionId=5&_a=summary"><img src="https://img.shields.io/azure-devops/build/cugu/dfir/5" alt="build" /></a>
 <a href="https://dev.azure.com/cugu/dfir/_build?definitionId=5&_a=summary"><img src="https://img.shields.io/azure-devops/coverage/cugu/dfir/5" alt="coverage" /></a>
</p>

## Installation

``` bash
pip install ksylint
```

## Usage
``` bash
ksylint hello_world.ksy
```

### Missing style guide tests (TODO)
1. General formatting
    - Use block YAML style in most general cases, unless explicitly specified/allowed otherwise.
    - Formatting of maps-inside-sequences MUST have - delimiter and first map element on the same first line.
3. Meta section (meta)
    - xref — keys inside MUST be in alphabetic order
    - license — MUST be a valid SPDX license expression
    - ks-version — SHOULD list lowest possible KS compiler version that is able to compile this file.
    - 	KS syntax allows usage of some top-level elements deep inside the hierarchy — this can be useful during development, for example, for purpose of grafting one .ksy file into another quickly. However, in production-quality .ksy files, one MUST NOT use keys like title, imports or ks-version (i.e. everything except explicitly listed in a list above) on intermediate levels.
    - The following keys are reserved for internal use (i.e. debugging and test running) and MUST NOT be used in general-purpose .ksy files: ks-debug, ks-opaque-types
4. Documentation
    - Single-line documentation strings SHOULD BE formatted using raw unquoted string literals.
    - Multi-line SHOULD BE formatted using YAML literal style scalar, i.e. using : | syntax.
    - Lines should be wrapped to be 80 columns long. If it doesn’t fit into single line after wrapping, then it’s a multi-line docstring, so use proper multi-line syntax.
    - There is no formal conversion of docstrings into language-specific docstrings now in KS, but generally we SHOULD keep it close to CommonMark formatting, i.e.:
        - paragraphs separated by an empty line
        - bullet lists created by an asterisk * and a space at the beginning of the line
        - use backticks ` to wrap identifiers and small pieces of code
5. Sequence attributes
    - Attribute identifiers
    - Trailing padding

### Not checked
- All identifiers, docstrings, comments and generally all human-readable text SHOULD be kept in English, unless there’s a very good reason not to do so.
- application — SHOULD name a particular application, if there’s any; if there are too many to list (for example, network packet formats or executables are used virtually everywhere), then one SHOULD omit this field.
- file-extension — if there’s only one extension, MUST be a string; if there are several, MUST be an sequence in block form and SHOULD order extensions from most popular extension to least popular.