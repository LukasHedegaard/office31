from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="office31",
    version="0.1.3",
    author="Lukas Hedegaard",
    description="Revised splits for Office31 domain adaptation experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukasHedegaard/office31",
    python_requires=">=3.6",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["datasetops==0.0.6", "requests"],
    extras_require={
        "tests": ["pytest", "pytest-cov"],
        "build": ["setuptools", "wheel", "twine"],
    },
)
