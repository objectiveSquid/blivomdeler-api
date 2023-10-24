from setuptools import find_packages, setup

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",
    "Natural Language :: English",
    "Natural Language :: Danish",
]

KEYWORDS = ["python", "api", "api-wrapper", "blivomdeler"]

DEPENDENCIES = ["requests"]
VERSION = "0.1.0"
NAME = "blivomdeler-api"
AUTHOR_NAME = "Magnus Zahle"
AUTHOR_EMAIL = "objectivesquid@outlook.com"
LICENSE = "MIT"
GITHUB_URL = "https://github.com/objectiveSquid/blivomdeler-api"

SHORT_DESCRIPTION = (
    "A python library for doing all sorts of things on the https://blivomdeler.nu site."
)
with open("README.md", "r") as readme_file, open("CHANGELOG.md", "r") as changelog_file:
    LONG_DESCRIPTION = f"{readme_file.read()}\n\n{changelog_file.read()}"

setup(
    name=NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
)
