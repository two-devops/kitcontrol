from setuptools import setup, find_packages


setup(
    name='kitcontrol',
    version='1.0.0',
    package_dir={"": "kitcontrol"},
    packages=find_packages("kitcontrol"),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'kitcontrol = main:cmd',
        ],
    },
)
