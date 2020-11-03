from setuptools import find_packages, setup


setup(
    name="starwars",
    version="0.0.1",
    description="Star wars dice rollers and other goodies",
    python_requires=">=3.7.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
)
