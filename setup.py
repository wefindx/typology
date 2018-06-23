from setuptools import find_packages, setup

setup(
    name='typology',
    version='0.0.3',
    description='Python formats derived from vocabulary concepts.',
    url='https://gitlab.com/wefindx/typology',
    author='Mindey',
    author_email='mindey@qq.com',
    license='ASK FOR PERMISSIONS',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=['requests'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False
)