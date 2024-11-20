from ustfile import validating_password
from read import read_file
for i in read_file():
    out = validating_password(i)
    print(out)
