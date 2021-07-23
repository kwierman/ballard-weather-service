from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='ballard_weather_service',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Air Quality Data Provider for Ballard",
    license="MIT",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/ballard_weather_service',
    packages=['ballard_weather_service'],
    entry_points={
        'console_scripts': [
            'ballard_weather_service=ballard_weather_service.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='ballard_weather_service',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
