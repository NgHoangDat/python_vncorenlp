import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_vncorenlp",
    packages=setuptools.find_packages(),
    version="0.1.0",
    author="nghoangdat",
    author_email="18.hoang.dat.12@gmail.com",
    description="python_vncorenlp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python-vncorenlp vncorenlp nlp vietnamese-nlp parser word-segmentation tokenizer pos-tagger '
               'named-entity-recognition ner dependency-parser',
    url="https://github.com/NgHoangDat/python_vncorenlp.git",
    download_url="https://github.com/NgHoangDat/python_vncorenlp/archive/v0.1.0.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'pyjnius',
        'typing-extensions'
    ]
)