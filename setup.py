from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cc1_levelset_transformer',
    url='https://github.com/ChipMcCallahan/CC1LevelsetTransformer',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['cc1_levelset_proto @ git+https://github.com/ChipMcCallahan/CC1LevelsetProto'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU General Public License v3.0',
    description='Transforms CC1 Levelsets by tile replacement, e.g. into "walls of"',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)