from setuptools import setup, find_packages


setup(
    name='kitcontrol',
    version='1.0.0',
    package_dir={"": "kitcontrol"},
    packages=find_packages("kitcontrol"),
    install_requires=[
        'Click',
        'Mockito',
        'pyyaml',
        'utils',
        'mergedeep',
        'fabric',
        'decorator',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'kitcontrol = main:command',
        ],
    },
)
