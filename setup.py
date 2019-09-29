from setuptools import setup

setup(
    name='ksylint',
    version='0.1',
    description='A linter for ksy files.',
    url='http://github.com/cugu/ksylint',
    author='Jonas Plum',
    license='GPL-3.0-or-later',
    packages=['lint'],
    entry_points={
        'console_scripts': [
            'ksylint=lint.lint:main',
        ],
    },
    install_requires=[
        "yamllint==1.17.0",
        "jsonschema==3.0.2",
        "PyYAML==5.1.2",
    ],
    package_data={
        'lint': ['ksy_schema.json'],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
