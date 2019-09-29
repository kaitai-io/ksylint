
YAMLLINT_RULES = """---

yaml-files:
  - '*.ksy'

rules:
  braces: disable
  brackets: disable
  colons: disable
  commas: disable
  comments: disable
  comments-indentation: disable
  document-end: disable
  document-start:
    present: false
  empty-lines: disable
  empty-values: disable
  hyphens:
    max-spaces-after: 1
  indentation:
    spaces: 2
    indent-sequences: true
  key-duplicates: disable
  key-ordering: disable
  line-length: disable
  new-line-at-end-of-file: enable
  new-lines:
    type: unix
  octal-values: disable
  quoted-strings: disable
  trailing-spaces: disable
  truthy: disable
"""
