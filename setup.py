import pathlib
import setuptools

setuptools.setup(
	    name='flowde',
	    version='0.0.4',
	    description='Flowde is a simple PY library to help you out with coding in python.',
	    long_description=pathlib.Path('README.md').read_text(),
	    long_description_content_type='text/markdown',
	    author='General Zero',
	    author_email='GeneralZeroCosmo@gmail.com',
	    license='Apache Software License 2.0',
	    classifiers=[
	    "Intended Audience :: Developers",
	    "Natural Language :: English",
	    "Programming Language :: Python :: 3",
	    "Programming Language :: Python :: 3.10",
	    "Programming Language :: Python :: 3.11",
	    "Development Status :: 3 - Alpha",
	    "License :: OSI Approved :: Apache Software License",
            "Topic :: Utilities"
	    ],
	    python_requires='>=3.10',
	    install_requires=['requests', 'colorama'],
	    packages=setuptools.find_packages(),
	    include_package_data=True,
	    entry_points={"console_scripts": ["flowde = flowde.cli:main"]},
)
