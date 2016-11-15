import setuptools

setuptools.setup(
    name='greeter',
    version='0.0.1',
    author='Moshe Zadka',
    author_email='moshe.zadka@clusterhq.com',
    packages=setuptools.find_packages(),
    install_requires=['flask'],
)
