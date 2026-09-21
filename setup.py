from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements list.
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements




setup(
    name='CreditPulse',
    version='1.0',
    author='Rugved Deshwant',
    author_email='rsdeshwant@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)