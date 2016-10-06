from setuptools import setup, find_packages

setup(
    name='repo-reader',
    version='0.2.0',
    author='Nathan Taylor',
    author_email='nathan.taylor.oss@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests>=2.11.0'],
    extras_require={'test': ['httpretty']}
)
