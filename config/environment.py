import os
#operating system i.e mac osx or windows 10 etc probably because this is stored on our computers hard drive or RAM
secret = os.getenv('SECRET', 'something good')
