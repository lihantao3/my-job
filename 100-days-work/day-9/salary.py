"""
工资结算系统
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import abstractmethod, ABCMeta


class Employee(object, metaclass=ABCMeta):
    """员工基类"""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        计算月薪
        :return: 月薪
        """
        pass


class Manager(Employee):
    """部门经理， 月薪15000"""
    def get_salary(self):
        return 15000.00


class Programmer(Employee):
    """程序员，月薪按工作时间计算，每小时150"""
    def __init__(self, name, working_hours=0):
        super(Programmer, self).__init__(name)
        self._working_hours = working_hours

    @property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours):
        self._working_hours = working_hours if working_hours > 0 else 0

    def get_salary(self):
        return self._working_hours * 150.00

class Salesman(Employee):
    """销售员,月薪是1200元的底薪加上销售额5%的提成"""
    def __init__(self, name, sales=0):
        super(Salesman, self).__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self) -> float:
        return 1200.00 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hours = int(input('请输入%s本月的工作时长：' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月的销售额：' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为：￥%.2f元。' % (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()


