import setuptools

setuptools.setup(
    name='temporal_proto',
    description='package of python files generated from temporal protos',
    author='Chris Vanderschuere',
    author_email='christopher.vanderschuere@gmail.com',
    version='1.0.1',
    url='https://github.com/cvanderschuere/temporal-proto-python',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'protobuf',
        'grpcio-tools',
    ]
)
