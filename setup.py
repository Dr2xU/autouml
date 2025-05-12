from setuptools import setup, find_packages
import pathlib

# Read the contents of your README file
this_dir = pathlib.Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name='autouml',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'autouml=autouml.cli.entrypoint:main'
        ]
    },
    author='Dr2xU',
    author_email='w.akil@hotmail.com',
    description='Generate UML class diagrams from Python projects using PlantUML',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Dr2xU/autouml',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
    ],
    python_requires='>=3.7',
)
