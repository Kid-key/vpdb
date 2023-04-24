from setuptools import setup, find_packages
import glob

setup(
    name="vpdb",
    version="1.1.0",
    author="Dechao Meng",
    author_email="dechao.meng@vipl.ict.ac.cn",
    url="https://github.com/Kid-key/vpdb",
    # keywords=("vscode", "launch"),
    description="Python debug configuration generator for vscode",
    scripts=glob.glob('scripts/*'),
    # long_description="",
    packages=find_packages(exclude=('examples', 'examples.*')),
)
