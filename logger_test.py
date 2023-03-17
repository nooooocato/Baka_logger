from super_logger import SuperLogger

for i in range(20):
    SuperLogger('info',i,'./test.log')
    SuperLogger('error',i,'./test.log')
    SuperLogger('info',i,'./test1.log')
    SuperLogger('error',i,'./test1.log')