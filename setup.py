from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="pyedalib",
    version="0.0.4",
    author="Atin Maiti",
    author_email="maiti.atin@gmail.com",
    description="A package easy eda",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Data-Saavy-Science/pyedalib",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)