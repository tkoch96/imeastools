from setuptools import find_packages, setup
setup(
	name='imeastools',
	packages=find_packages(include=['imeastools']),
	version='0.1.0',
	description='Useful Internet measurement tools.',
	author='Tom Koch',
	license='MIT',
	install_requires=['numpy', 'geopy', 'cymruwhois', 'azure-kusto-data', 'azure-kusto-ingest', 'azure-core'],
	setup_requires=['pytest-runner'],
	tests_require=['pytest==4.4.1'],
	test_suite='tests',
)