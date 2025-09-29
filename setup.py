import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='5.1.0',
    description='Python project',
    author='Anurag Pandey',
    author_email='anuragpandey12@gmail.com',
    url='https://github.com/Anurag637/Audio-Speech-To-Sign-Language-Converter.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)