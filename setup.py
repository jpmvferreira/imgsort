from setuptools import setup

with open(f"README.md") as f:
    long_description = f.read()

setup(name="imgsort",
      version="1.0.0",
      description="A terminal utility to sort image files based on their characteristics.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=[
        "Pillow",
      ],
      url="https://github.com/jpmvferreira/imgsort",
      author="José Ferreira",
      author_email="jose@jpferreira.me",
      license="MIT",
      scripts=["bin/imgsort"],
      zip_safe=False)
