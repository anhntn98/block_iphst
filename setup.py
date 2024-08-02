from setuptools import find_packages, setup

setup(
    name='block_iphst',
    version='0.3.5',
    description='Block IP zone hosting',
    install_requires=['junos-eznc'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
