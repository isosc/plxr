from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='plxr',
      version='0.2.dev1',
      description='tools for leveraging self-describing data storage',
      url='https://github.com/isosc/plxr',
      author='Jeremy Logan',
      author_email='lot@ornl.gov',
      license='Apache 2.0',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['plxr'],
      install_requires=['pillow','matplotlib'],
      scripts=['scripts/plxr','scripts/bpix','scripts/bpview','scripts/bpmerge'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
