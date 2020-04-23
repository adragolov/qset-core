import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="qset-core-adragolov",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Atanas Dragolov",
    author_email="adragolov@gmail.com",
    description="Core redistributable of the Quantset toolbox.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adragolov/qset-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
