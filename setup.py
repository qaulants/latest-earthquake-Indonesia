import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latest-earthquake-bmkg",
    version="0.3",
    author="Qaulan Tsaqila",
    author_email="qaulantsaqila75@gmail.com",
    description="This package will get latest earthquake from BMKG | Meteorological, Climatological, and Geophysical "
                "Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qaulants/latest-earthquake-Indonesia",
    project_url={
        "Website": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],

    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
