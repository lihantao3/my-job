#奥特曼打小怪兽

from abc import abstractmethod, ABCMeta
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    #战斗着
    #通过__slots__限定属性

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """初始化方法
        name：名字
        hp：血量
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击
        other： 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    '''奥特曼'''

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super(Ultraman, self).__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技，打掉对方至少50点或四分之三的血量
        :param other: 被攻击的对象
        :return: 使用成功返回True否则False
        """

        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击，aoe伤害
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True否则False
        """

        if self._mp >= 20:
            self._mp -= 20
            for other in others:
                if other.alive:
                    other.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """回蓝"""

        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    """怪兽，只有普通攻击"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值：%d\n' % self._hp
    

def select_alive_one(monsters):
    """选中一只活着的怪兽"""
    monster_len = len(monsters)
    while True:
        index = randrange(monster_len)
        monster = monsters[index]
        if monster.alive:
            return monster

def is_any_alive(monsters):
    """判断有没有活着的怪兽"""
    for monster in monsters:
        if monster.alive:
            return True
        return False

def display_info(ultraman, monsters):
    """显示奥特曼和怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('泰罗奥特曼', 1000, 120)
    m1 = Monster('贝塔星人', 250)
    m2 = Monster('虚空行者', 500)
    m3 = Monster('怪兽王', 750)
    monsters = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(monsters):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(monsters)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击击打了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复%d点' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(monsters):
                print('%s使用了魔法攻击。' % u.name)
            else:
                print('%s使用魔法攻击失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了究极必杀技攻击%s' % (u.name, m.name))
            else:
                print('%s使用普通攻击击打了%s' % (u.name, m.name))
                print('%s的魔法值恢复%d点' % (u.name, u.resume()))
        if m.alive > 0:
            m.attack(u)
            print('%s回击了%s。' % (m.name, u.name))
        display_info(u, monsters)
        fight_round += 1
    print('\n========战斗结束=========\n')
    if u.alive:
        print('%s胜利！' % u.name)
    else:
        print('怪兽军团胜利')


if __name__ == '__main__':
    main()
