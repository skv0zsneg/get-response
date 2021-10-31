import setuptools


VERSION = '0.0.1'
NAME = 'get_response'
AUTHOR = 'skvozsneg'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description="Api response tool for easy parsing REST and SOAP API responses.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/skvozsneg/api-response",
    project_urls={
        "Bug Tracker": "https://github.com/skvozsneg/api-response/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
