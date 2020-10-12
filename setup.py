import setuptools

_pkg_version = "1.0.1"
_author = "Thomas McGowan"
_author_email = "mcgo0092@umn.edu"
_license = "MIT"
_repo = "https://github.umn.edu/mcgo0092/psm_fragments.git"


setuptools.setup(
    name="psm_fragments",
    version=f"{_pkg_version}",
    packages=["psmfragmentation"],
    install_requires=["numpy", "lxml", "pyteomics", "plotly"],
    description="Score PSMs with fragmentation quality check",
    author=f"{_author}",
    author_email=f"{_author_email}",
    url="f{_repo}",
    download_url=f"{_repo}/archive/v_{_pkg_version}.tar.gz",
    license=f"{_license}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.6",
)
