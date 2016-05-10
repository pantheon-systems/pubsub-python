from setuptools import setup, find_packages


setup(
    name='pubsub-python',
    version='0.1',
    url="https://github.com/pantheon-systems/pubsub-python@master",
    description='pubsub client wrappers',
    long_description='',
    author='Michael Liu',
    author_email='michael.liu@getpantheon.com',
    license='BSD',
    keywords='pubsub'.split(),
    platforms='any',
    packages=find_packages(include=['pubsub.*', 'pubsub_etl.*']),
    include_package_data=False,
    #test_suite='test_dashvisor.run_tests.run_all',
    install_requires=[
        "google-api-python-client>=1.5.0"
    ],
)
