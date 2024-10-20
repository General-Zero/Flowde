import pathlib
import setuptools

setuptools.setup(
	    name='flowde',
	    version='0.0.1',
	    description='Flowde is a simple PY library.',
	    long_description=pathlib.Path('README.md').read_text(),
	    long_description_content_type='text/markdown',
	    author='Cosmo',
	    author_email='jayraldvax@gmail.com',
	    license='MIT License',
	    classifiers=[
	    "Intended Audience :: Developers",
	    "Programming Language :: Python :: 3.10",
	    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
    "Topic :: Utilities"
	    ],
	    python_requires='>=3.10',
	    install_requires=['requests'],
	    packages=setuptools.find_packages(),
	    include_package_data=True,
	    entry_points={
    "console_scripts": [
        "flowde = flowde.cli:main"]
},
)
