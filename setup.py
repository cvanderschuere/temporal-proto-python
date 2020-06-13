import setuptools

setuptools.setup(
    name='temporal',
    description='package of python files generated from temporal protos',
    author='Chris Vanderschuere',
    author_email='christopher.vanderschuere@gmail.com',
    version='0.0.1',
    url='https://github.com/cvanderschuere/temporal-python',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'protobuf',
        'grpcio-tools',
    ]
)
