from distutils.core import setup
import glob
setup(
    name='blog',
    version='1.0',
    description='blog',
    author='wang',
    packages=['blog','post','users'],
    py_modules=['manage'],
    data_files=glob.glob('templates/*.html')+['requirements']
)