import os

username = 'hdnclocdyumyoo'
password = '7d413f1d10a1f54e123d52fe732c9d3c9617e39c58cb723a50961293af8d9412'
host = 'ec2-54-225-129-101.compute-1.amazonaws.com'
port = '5432'
database = 'd811f7gneghqgf'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://hdnclocdyumyoo:7d413f1d10a1f54e123d52fe732c9d3c9617e39c58cb723a50961293af8d9412@ec2-54-225-129-101.compute-1.amazonaws.com:5432/d811f7gneghqgf')