import re
strt='''echo $(ps -ef|grep httpd)


BusyBox v1.17.2 (2016-06-01 09:57:40 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

# echo $(ps -ef|grep httpd)
786 0 8568 S httpd -S -E /usr/sbin/ca.pem /usr/sbin/httpsd.pem 3906 0 1912 S grep httpd
# '''
def get_PID(result):
    # lists=result.split('\n')
    # for ret in lists:
        reg=re.compile(r'\d{3}\s')
        tmp = re.findall(reg, result)
        if tmp:
            print(tmp)

        # if tmp:
        #     tmp=tmp.group()
        #     tmp=tmp.replace(' ', '')
            
        #     PID = tmp
        #     print(PID)
if __name__ == "__main__":
    get_PID(strt)