from setuptools import setup

setup(
    name='lmapi',
    version='1.0.0',
    url='https://github.com/ElonMax/lm-api',
    package_dir={"": "src"},
    install_requiers=[
        'requests==2.31.0',
    ]
)
