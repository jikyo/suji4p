try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='suji',
    version='0.1.0',
    description='Japanese number notation converter',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    author='Junnosuke Moriya',
    author_email='shinsen.jikyo@gmail.com',
    url='https://github.com/jikyo/suji4p',
    license='Apache License 2.0',
    packages=['suji'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Natural Language :: Japanese',
    ],
)
