from setuptools import setup, find_packages

setup(
    name='robobo_emotion',
    version='0.1',
    url="https://github.com/Calza36/roboboemotions",
    author="Ernesto Calzadilla",
    description="Librería para detectar emociones en imágenes y audio usando Robobo",
    py_modules=['robobo_emotion'],
    packages=find_packages(),
    install_requires=[
        'absl-py==2.1.0',
        'asttokens==2.2.1',
        'astunparse==1.6.3',
        'attrs==23.2.0',
        'backcall==0.2.0',
        'beautifulsoup4==4.12.3',
        'blinker==1.7.0',
        'cachetools==5.3.2',
        'certifi==2024.2.2',
        'cffi==1.16.0',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'colorama==0.4.6',
        'comm==0.1.2',
        'contourpy==1.2.0',
        'cycler==0.12.1',
        'deepface==0.0.84',
        'debugpy==1.6.6',
        'decorator==5.1.1',
        'dlib==19.24.2',
        'executing==1.2.0',
        'facenet-pytorch==2.5.3',
        'filelock==3.13.1',
        'fire==0.5.0',
        'Flask==3.0.2',
        'flatbuffers==23.5.26',
        'fonttools==4.48.1',
        'fsspec==2024.2.0',
        'gast==0.5.4',
        'gdown==5.1.0',
        'google-auth==2.27.0',
        'google-auth-oauthlib==1.2.0',
        'google-pasta==0.2.0',
        'grpcio==1.60.1',
        'gunicorn==21.2.0',
        'h5py==3.10.0',
        'idna==3.6',
        'ipykernel==6.21.3',
        'ipython==8.11.0',
        'itsdangerous==2.1.2',
        'jedi==0.18.2',
        'Jinja2==3.1.3',
        'jupyter_client==8.0.3',
        'jupyter_core==5.3.0',
        'keras==2.15.0',
        'keyboard==0.13.5',
        'kiwisolver==1.4.5',
        'libclang==16.0.6',
        'Markdown==3.5.2',
        'MarkupSafe==2.1.5',
        'matplotlib==3.8.2',
        'matplotlib-inline==0.1.6',
        'mediapipe==0.10.9',
        'ml-dtypes==0.2.0',
        'mpmath==1.3.0',
        'mtcnn==0.1.1',
        'nest-asyncio==1.5.6',
        'networkx==3.2.1',
        'numpy==1.26.4',
        'oauthlib==3.2.2',
        'opencv-contrib-python==4.9.0.80',
        'opencv-python==4.9.0.80',
        'opt-einsum==3.3.0',
        'packaging==23.0',
        'pandas==2.2.0',
        'parso==0.8.3',
        'pickleshare==0.7.5',
        'pillow==10.2.0',
        'prompt-toolkit==3.0.38',
        'protobuf==3.20.3',
        'psutil==5.9.4',
        'pure-eval==0.2.2',
        'py-cpuinfo==9.0.0',
        'pyasn1==0.5.1',
        'pyasn1-modules==0.3.0',
        'PyAudio==0.2.14',
        'pycparser==2.21',
        'Pygments==2.14.0',
        'pyparsing==3.1.1',
        'PySocks==1.7.1',
        'python-dateutil==2.8.2',
        'pytz==2024.1',
        'pywin32==305',
        'PyYAML==6.0.1',
        'pyzmq==25.0.1',
        'requests==2.31.0',
        'requests-oauthlib==1.3.1',
        'retina-face==0.0.14',
        'robobopy==1.3.3',
        'robobopy-audiostream==1.1.0',
        'robobopy-videostream==1.0.1',
        'rsa==4.9',
        'scipy==1.12.0',
        'seaborn==0.13.2',
        'six==1.16.0',
        'sounddevice==0.4.6',
        'soupsieve==2.5',
        'stack-data==0.6.2',
        'sympy==1.12',
        'tensorboard==2.15.2',
        'tensorboard-data-server==0.7.2',
        'tensorflow==2.15.0',
        'tensorflow-estimator==2.15.0',
        'tensorflow-intel==2.15.0',
        'tensorflow-io-gcs-filesystem==0.31.0',
        'termcolor==2.4.0',
        'thop==0.1.1.post2209072238',
        'torch==2.2.0',
        'torchvision==0.17.0',
        'tornado==6.2',
        'tqdm==4.66.1',
        'traitlets==5.9.0',
        'typing_extensions==4.9.0',
        'tzdata==2023.4',
        'ultralytics==8.1.11',
        'urllib3==2.2.0',
        'wcwidth==0.2.6',
        'websocket-client==1.7.0',
        'Werkzeug==3.0.1',
        'wrapt==1.14.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)