from setuptools import setup

setup(
    name="zkdaddy",
    version="0.1",
    py_modules="zkdaddy",
    install_requires=['click==7.1.2', 'colorama==0.4.4', 'kazoo==2.8.0', 'pydantic==1.8.1', 'six==1.15.0',
                      'typing-extensions==3.7.4.3'],
    scripts=['main'],
    author="daryl",
    author_email="susecjh@gmail.com",
)
