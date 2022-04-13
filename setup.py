from setuptools import setup

version = "0.1.dev0"

long_description = "\n\n".join([open("README.rst").read(), open("CHANGES.rst").read()])

install_requires = [
    "aiofiles",
    "aiohttp",
    "click",
    "h5py",
    "jwt",
    "netCDF4",
    "pyjwt==1.7.1",
    "requests",
    "pandas",
    "threedi-api-client>=4.0.0",
    "threedigrid>=1.0.16",
    "threedi-modelchecker==0.25.3",
]

tests_require = [
    "pytest",
    "mock",
    "pytest-cov",
    "pytest-flakes",
    "pytest-black",
    "threedi-api-client",
    "requests",
]

setup(
    name="batch-calculator",
    version=version,
    description="3Di batch calculations",
    long_description=long_description,
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Programming Language :: Python", "Framework :: Django"],
    keywords=[],
    author="Wout Lexmond",
    author_email="wout.lexmond@nelen-schuurmans.nl",
    url="https://github.com/nens/batch-calculator",
    license="MIT",
    packages=["batch_calculator"],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    entry_points={
        "console_scripts": [
            "run-rain-series-simulation = batch_calculator.rain_series_simulations:create_rain_series_simulations",
            "download-rain-series-results = batch_calculator.process_results:process_results",
        ]
    },
)
