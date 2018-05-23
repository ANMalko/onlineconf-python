from setuptools import setup

setup(
    name='onlineconf',
    version='0.0.1',
    url='https://gitlab.corp.mail.ru/myspb/common/onlineconf',
    author='mail.ru',
    packages=['.'],
    install_requires=[
        'pure-cdb==2.0.1',
        'aiofiles==0.3.2'
    ]
)