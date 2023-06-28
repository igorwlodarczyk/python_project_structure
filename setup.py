from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="py_project",
    version="0.1.0",
    author="Igor Wlodarczyk",
    author_email="wlodar.igor@gmail.com",
    description="py_project",
    long_description=long_description,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    setup_requires=[""],
    install_requires=[""],
)
