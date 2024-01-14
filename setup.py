from setuptools import setup, find_packages

setup(
    name="Monnify",
    version="1.0.0",
    description="A Python package for Monnify integration",
    long_description=open("README.md").read(),
    author="Abdulhaleem Nasredeen",
    author_email="nabdulhaleem09@gmail.com",
    url="https://github.com/nasredeenabdulhaleem/monnify",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests",
        # Add any other dependencies here
    ],
    # Add any additional keywords that describe your package here
    keywords="Monnify, Python, Payment, Integration, Africa, Nigeria, Africa, Payment Gateway, Payment Integration, Payment API, Payment Nigeria, Payment Africa, Payment Gateway Nigeria, Payment Gateway Africa, Payment API Nigeria, Payment API Africa, Payment Gateway API, Payment Gateway API Nigeria, Payment Gateway API Africa, Payment Gateway Integration, Payment Gateway Integration Nigeria, Payment Gateway Integration Africa, Payment Gateway Integration API, Payment Gateway Integration API Nigeria, Payment Gateway Integration API Africa, Payment Gateway Integration Africa Nigeria, Payment Gateway Integration Nigeria Africa, Payment Gateway Integration Nigeria API, Payment Gateway Integration Africa API, Payment Gateway Integration Nigeria Africa API",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
