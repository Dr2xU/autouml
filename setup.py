from setuptools import setup, find_packages

setup(
    name='autouml',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'autouml=autouml.cli.entrypoint:main'
        ]
    },
    author='Your Name',
    author_email='you@example.com',
    description='Generate UML class diagrams from Python projects using PlantUML',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/autouml',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
