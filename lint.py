#!/usr/bin/env python3

from jsonschema import Draft7Validator
from yamllint import linter, config
import argparse
import os.path as path
import sys
import yaml

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


def lint_file(filename):
    return_code = 0
    print(filename)

    # validate filename
    if not filename.endswith(".ksy"):
        print("File names should end with .ksy")
        return_code += 1

    # validate encoding
    with open(filename, 'rb') as f:
        try:
            f.read().decode('utf-8')
        except UnicodeError:
            print("string is not UTF-8")
            return_code += 1

    with open(filename) as f:
        conf = config.YamlLintConfig(content=YAMLLINT_RULES)

        # lint file
        for problem in linter.run(f, conf):
            print(problem)
            return_code += 1

        f.seek(0, 0)

        # validate schema
        try:
            inst = yaml.load(f)
            with open("ksy_schema.json") as schema_io:
                schema = yaml.load(schema_io)

                v = Draft7Validator(schema)
                try:
                    for error in v.iter_errors(inst):
                        print(error.message)
                        return_code += 1
                except Exception as e:
                    print("Validation failed. %s" % e)
                    return_code += 1

            mname = inst['meta']['id'] + ".ksy"
            if not mname == path.basename(filename):
                print("meta.id must match filename %s %s" % (mname, filename))
                return_code += 1

        except yaml.composer.ComposerError:
            pass
        except Exception as e:
            print("YAML parsing failed. %s" % e)
            return_code += 1

    return return_code


def main(args):
    return_code = 0
    for file in args.files:
        return_code += lint_file(file)
    return return_code


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lint Kaitai Struct files.")
    parser.add_argument('files', type=str, nargs='+')

    args = parser.parse_args()

    sys.exit(main(args))
