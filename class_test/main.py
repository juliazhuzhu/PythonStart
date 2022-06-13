#封装的问题
#栈

from collections import namedtuple


NewCourse = namedtuple('Course', 'name price url')

a = NewCourse(name='django', price=100, url="http://hlgnet.com")
course2 = []

course2.append(a)

