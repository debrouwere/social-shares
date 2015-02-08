from setuptools import setup, find_packages


setup(name='socialshares',
    description='A command-line and programmatic interface to various social sharecount endpoints.',
    long_description=open('README.rst').read(),
    author='Stijn Debrouwere',
    author_email='stijn@debrouwere.org',
    url='https://github.com/debrouwere/social-shares',
    download_url='https://github.com/debrouwere/social-shares/tarball/master',
    version='1.0.0',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics facebook twitter googleplus pinterest',
    entry_points = {
          'console_scripts': [
                'socialshares = socialshares.command:main', 
          ],
    }, 
    test_suite='socialshares.tests', 
    install_requires=[
        'docopt', 
        'requests', 
    ], 
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],
    )
