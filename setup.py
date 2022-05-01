import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="APILib",
    version="1.0.0",
    author="SomeHybrid",
    author_email="lacannguyenvn@gmail.com",
    description="A package for helping use APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SomeHybrid/apilib/",
    project_urls={
        "Bug Tracker": "https://github.com/SomeHybrid/apilib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Framework :: aiohttp",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Session"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)