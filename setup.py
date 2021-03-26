from setuptools import setup 

setup(
	name ="speech_text",
	version = "speech-text>=1.0.0",
	description = "Converts spoken english text to written english text",
	long_description = "Converts a paragraph of spoken english to written english. For example, two dollars is converted to $2. Tripple A is converted to AAA, C M to CM, etc", 
	author = "Rishikesh Fulari",
	packages = ['speech_text'])