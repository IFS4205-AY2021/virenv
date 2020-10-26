import os
import random
f=open('MOCK_DATA.csv','r')
f_w=open('data.csv','w')
f_auth=open('auth.sql','w')
f_userinfo=open('userinfo.sql','w')
f_auth_group=open('auth_group.sql','w')

f.readline()
f_auth.write('USE subsys_admin;\n')
f_userinfo.write('USE subsys_admin;\n')
f_auth_group.write('USE subsys_admin;\n')

def getTestResult():
    ratio = 0.1
    if random.random() < ratio:
        return 'True'
    else:
        return 'False'

count = 1
s = set()
for line in f:
    l = line.split(',')
    l[0] = l[0].replace("'",'')
    l[1] = str(random.randint(80,99)) + l[1][-6:]                   # phone
    l[2] = str(random.randint(19,85))                               # age
    l[3] = l[3]                                                     # gender
    l[4] = ''.join(list('0' + str(random.randint(1,81)))[-2:]) + ''.join(list('000' + str(random.randint(1,9999)))[-4:])      # location
    l[5] = ''.join(list('0000' + str(random.randint(1,999)))[-4:])  # address
    l[6] = getTestResult()                                          # test result
    l += [str(count)]                                               # id

    username = l[0].split(' ')[0].lower() + l[0].split(' ')[1][0].lower()
    if username in s:
        continue
    s.add(username)

    # ["Eleanora O'Dare", '1237405410', '22', 'F', '4 Schlimgen Road', '069 Lighthouse Bay Street', 'true\n']

    # INSERT INTO `user_userinfo` VALUES (1,'Zhang Jing','93925044',21,'118686','0123','False','',2,'NA');
    sql = "INSERT INTO `user_userinfo` VALUES (" +str(count + 3)+ ",'"+ l[0] +"','" + l[1] + "'," + l[2] + ",'" + l[4] + "','" + l[5] + "','" + l[6] + "','" + "None" + "'," + str(count + 5) + ",'"+ l[3] +"');"
    f_userinfo.write(sql+'\n')

    # (2,'hash','2020-10-19 03:16:06.481158',0,'jc1','','','jc1@jc.com',0,1,'2020-10-19 02:42:37.614558')
    sql_auth = "INSERT INTO `auth_user` VALUES (" + str(count + 5) + ",'hash','2020-10-15 02:40:18.308951',0,'" + l[0].split(' ')[0].lower() + l[0].split(' ')[1][0].lower() + "','','','',0,1,'2020-10-14 02:39:51.198748');"
    f_auth.write(sql_auth+'\n')

    sql_group = "INSERT INTO `auth_user_groups` VALUES (" + str(count + 2) + "," + str(count + 5) + ",2);"
    f_auth_group.write(sql_group+'\n')
    f_w.write(','.join(l))
    count += 1

f.close()
f_w.close()
f_auth.close()
f_userinfo.close()

# auth_user
# password varchar(128) 
# last_login datetime(6) 
# is_superuser tinyint(1) 
# username varchar(150) 
# first_name varchar(150) 
# last_name varchar(150) 
# email varchar(254) 
# is_staff tinyint(1) 
# is_active tinyint(1) 
# date_joined datetime(6)

# userinfo
# name varchar(64) 
# phone varchar(12) 
# age int UN 
# location varchar(6) 
# address varchar(16) 
# test_result varchar(5) 
# encryption_keys longtext 
# relate_id int 
# gender varchar(2)
