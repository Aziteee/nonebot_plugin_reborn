#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nonebot_plugin_reborn",
    version="0.1",
    description='Reborn Simulator for Nonebot 2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Azite',
    author_email='aziteee@outlook.com',
    license='MIT License',
    packages=["nonebot_plugin_reborn"],
    install_requires=[
        "nonebot2>=2.0.0b3",
        "nonebot-adapter-onebot>=2.0.0b1",
        "nonebot-plugin-htmlrender>=0.0.4",
    ],
    platforms=["all"],
    url='https://github.com/Aziteee/nonebot_plugin_reborn',
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
