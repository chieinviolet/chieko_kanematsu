try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='python_programming_demo_app',
    version='0.0.1',
    package=['suzuroboko','suzuroboko.controller','suzuroboko.models','suzuroboko.views'],
    url='https://note.example',
    license='MIT',
    author='chieko_kanematsu',
    author_email='example@gmail.com',
    long_description=open('readme.txt').read(),

)

