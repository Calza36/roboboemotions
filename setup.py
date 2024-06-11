from setuptools import setup, find_packages

setup(
    name='robobo_emotion',
    version='0.1',
    repository_url="https://github.com/Calza36/roboboemotions",
    py_modules=['robobo_emotion'],
    packages=find_packages(),
    install_requires=[
        'robobopy',
        'robobopy_videostream',
        'deepface',
        #'emotion2vec',
    ]  
)