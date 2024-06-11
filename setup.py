from setuptools import setup, find_packages

setup(
    name='robobo_emotion',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'robobopy',
        'robobopy_videostream',
        'deepface',
        'emotion2vec',
    ],
    entry_points={
        'console_scripts': [
            'robobo_emotion=robobo_emotion:main',
        ],
    },
)