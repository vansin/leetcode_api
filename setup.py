from setuptools import setup
import io
with io.open('readme.md', 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='leetcode_api',# 需要打包的名字,即本模块要发布的名字
    version='v0.5.5',#版本
    description='leetcode api', # 简要描述
    py_modules=['leetcode_api'],   #  需要打包的模块
    author='msnode', # 作者名
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='msnode@163.com',   # 作者邮件
    url='https://github.com/vansin/leetcode_api', # 项目地址,一般是代码托管的网站
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)