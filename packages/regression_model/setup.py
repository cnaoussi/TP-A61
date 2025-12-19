from setuptools import setup, find_packages

setup(
    name="regression_model",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "numpy>=1.18.1,<1.19.0",
        "pandas>=0.25.3,<0.26.0",
        "scikit-learn>=0.22.1,<0.23.0",
    ],
)