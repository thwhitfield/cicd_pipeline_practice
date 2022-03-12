"""Setup.py"""

import setuptools

setuptools.setup(
    name='cicd_pipeline_practice',
    version = '0.0.1',
    author = 'Travis Whitfield',
    description = "CI/CD Pipeline Practice",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.7'
)
