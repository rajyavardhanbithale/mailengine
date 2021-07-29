import setuptools



with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="mailengine",
    version="1.1",
    author="rajyavardhan_bithale",
    author_email="bithale03@protonmail.com",
    description="A Tool For Sending Mails And Send OTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/mailengine",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    packages=['mailengine'],
    package_data={'mailengine': ['*']},
    #include_package_data=True,
    python_requires=">=3.6",
)
