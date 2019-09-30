from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ksylint',
    version='0.3.1',
    description='A linter for ksy files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/cugu/ksylint',
    author='Jonas Plum',
    license='GPL-3.0-or-later',
    packages=['ksylint'],
    entry_points={
        'console_scripts': [
            'ksylint=ksylint.lint:main',
        ],
    },
    install_requires=[
        "yamllint==1.17.0",
        "jsonschema==3.0.2",
        "PyYAML==5.1.2",
    ],
    package_data={
        'ksylint': ['ksy_schema.json'],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
