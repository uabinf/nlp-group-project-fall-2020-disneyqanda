import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="disneyqanda", 
    version="0.0.1",
    author="Deeptha Srirangam, Leigh Allison",
    author_email="",
    description="Disney Q and A",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uabinf/nlp-group-project-fall-2020-disneyqanda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)