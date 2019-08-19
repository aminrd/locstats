import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "locstats",
    version = "0.0.1",
    author = "Dimitri Kokkonis",
    author_email = "kokkonisd@gmail.com",
    description = "A statistics tool for your LOC per language",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/kokkonisd/locstats",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)