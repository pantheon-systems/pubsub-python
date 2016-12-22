from setuptools import setup, find_packages


setup(
    name='gcloud-python',
    version='0.1',
    url="https://github.com/pantheon-systems/gcloud-python@master",
    description='gcloud client wrappers',
    long_description='',
    author='Michael Liu',
    author_email='michael.liu@getpantheon.com',
    license='BSD',
    keywords='gcloud'.split(),
    platforms='any',
    packages=find_packages(include=['gcloud_etl.*', 'clients.*']),
    include_package_data=False,
    #test_suite='test_dashvisor.run_tests.run_all',
    install_requires=[
        "google-api-python-client>=1.5.0"
    ],
)
