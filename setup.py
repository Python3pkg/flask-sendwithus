from setuptools import setup

setup(
    name='Flask-Sendwithus',
    version='1.0',
    author="Jacob Magnusson",
    author_email="m@jacobian.se",
    license="BSD",
    description="Forwards-compatible Flask extension to interact with the sendwithus API",
    packages=['flask_sendwithus'],
    install_requires=['flask>=0.8', 'sendwithus'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
