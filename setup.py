from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mpesa_daraja",
    version="0.0.22",
    description="Mpesa B2C, C2B, STKPush Python(Flask & Django) library based on the new Api's https://developer.safaricom.co.ke",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cephaske254/mpesa_daraja",
    author="Cephas Too",
    author_email="cephaske254@gmail.com",
    license="MIT",
    packages=["mpesa", "mpesa.api", "mpesa.tests"],
    zip_safe=False,
    python_requires=">=3.0",
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "certifi>=2019.11.28",
        "chardet>=3.0.4",
        "idna>=2.8",
        "requests>=2.22.0",
        "six>=1.14.0",
        "urllib3>=1.25.8",
        "webencodings>=0.5.1",
        "pytest>=3.6.1",
    ],
)