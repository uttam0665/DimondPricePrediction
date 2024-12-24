from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as s:
        requirements=s.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        return requirements

setup(
    name="Dimond Price Prediction",
    version='0.0.1',
    author='Uttam Gouda',
    author_email='goudauttam719@gmail.com',
    install_requires= get_requirements('requirements.txt'),
    packages=find_packages()
)