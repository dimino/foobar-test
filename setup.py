from setuptools import setup, find_packages


setup(
    name='foobar-test',
    version='0.0.0',
    packages=find_packages(),
    install_requires=['requests', 'kafka-python', 'psycopg2'],
    entry_points={
        'console_scripts': [
            'the-foobar-worker=foobar.foobar_one.service:main'
        ]
    }
)
