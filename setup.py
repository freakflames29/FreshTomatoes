import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
 name='freshtomatoes',
 version='0.2.1',
 author="Sourav Das",
 author_email="sourav292922@gmail.com",
 description="freshtomatoes will provide rottentomatoes scores of a given movie",
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/freakflames29/FreshTomatoes",
  project_urls={
        "Bug Tracker": "https://github.com/freakflames29/FreshTomatoes",
    },
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
)
