from setuptools import setup, find_packages

setup(
    name="auto-mail",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "jinja2>=3.0.0",
        "python-dotenv>=0.19.0"
    ],
    author="Nelson Daniels",
    author_email="nelsongdaniels@gmail.com",
    description="A package to automate email sending tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nelsonthelad/auto-mail",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
