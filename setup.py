from setuptools import setup


setup(
    name='foobar-test',
    version='0.0.0',
    packages=['foobar'],
    install_requires=['requests', 'kafka-python', 'psycopg2'],
    entry_points={
        'console_scripts': [
            'the-foobar-worker=foobar.foobar_two.service:main'
        ]
    }
)
