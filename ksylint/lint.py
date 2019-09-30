from jsonschema import Draft7Validator
from yamllint import linter, config
import argparse
import os
import os.path as path
import sys
import yaml
from . import order, yamllint_config


def lint_order(d):
    ret_code = 0

    keys = d.keys()
    key_order = list()
    for key in keys:
        if key in order.ORDER:
            key_order.append(order.ORDER[key])
        else:
            key_order.append(1000)
    if key_order != sorted(key_order):
        print("Keys are not ordered: %s" % list(keys))
        ret_code += 1

    for v in d.values():
        if isinstance(v, dict):
            ret_code += lint_order(v)

    return ret_code


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
        conf = config.YamlLintConfig(content=yamllint_config.YAMLLINT_RULES)

        # lint file
        for problem in linter.run(f, conf):
            print(problem)
            return_code += 1

        f.seek(0, 0)

        # validate schema
        try:
            inst = yaml.load(f, Loader=yaml.FullLoader)

            # validate schema
            return_code += lint_order(inst)

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(path.join(dir_path, "ksy_schema.json")) as schema_io:
                schema = yaml.load(schema_io, Loader=yaml.FullLoader)

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


def main():
    parser = argparse.ArgumentParser(description="Lint Kaitai Struct files.")
    parser.add_argument('files', type=str, nargs='+')

    args = parser.parse_args()

    return_code = 0
    for file in args.files:
        return_code += lint_file(file)

    sys.exit(return_code)


if __name__ == '__main__':
    main()
