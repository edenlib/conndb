from setuptools import setup

setup(
    name="conndb",  # this is what you pip install 'pip install name'
    version="0.0.1",
    description="Connect to a database.",
    py_modules=["conndb"],
    package_dir={"": "src"}
)
