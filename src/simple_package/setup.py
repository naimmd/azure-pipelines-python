import setuptools

print('dirname: ', os.path.dirname(__file__))
setuptools.setup(
    name="simple_package", version="0.0.2", packages=setuptools.find_packages()
)
