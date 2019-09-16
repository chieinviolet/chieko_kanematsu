try:
    from setuptools Import setup,find_packagena
except ImportError:
    from distutils.core import setup



setup(
name='python_programming_demo_app_suzu_roboko',
version='0.0.1'
packages=['suzuroboko','suzuroboko.models', 'suzuroboko.controller','suzuroboko.views'],
package_data={'suzuroboko':[]}
)
