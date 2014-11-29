from setuptools import setup, find_packages

setup(name='socialshares',
    description='A command-line and programmatic interface to various social sharecount endpoints.',
    long_description=open('README.rst').read(),
    author='Stijn Debrouwere',
    author_email='stijn@debrouwere.org',
    url='https://github.com/debrouwere/social-shares',
    download_url='https://github.com/debrouwere/social-shares/tarball/master',
    version='0.3.2',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics facebook twitter googleplus pinterest',
    entry_points = {
          'console_scripts': [
                'socialshares = socialshares.command:main', 
          ],
    }, 
    install_requires=[
        'docopt', 
        'requests', 
        'grequests', 
    ], 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],
    )
