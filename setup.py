from setuptools import setup, find_packages

setup(
    name="CryptoProject",
    version="0.1",
    packages=find_packages(where="src"),  # Specify `src` as the package root
    package_dir={"": "src"},             # Map the root package to `src`
)
