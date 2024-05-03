import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vidyasutra",
    version="0.1.0",
    author="Khushi Tiwari",
    author_email="khushitiwari014@gmail.com",
    description="A machine learning library for data manipulation, preprocessing, and model training.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vidyasutra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
    ],
)

