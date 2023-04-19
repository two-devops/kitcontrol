from setuptools import setup, find_packages


setup(
    name='ikcontrol',
    version='1.0.0',
    package_dir={"": "ikcontrol"},
    # packages=find_packages("ikcontrol"),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ikcontrol = main:cmd',
        ],
    },
)
