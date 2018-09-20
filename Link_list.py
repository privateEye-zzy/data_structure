'''
数据结构——单链表：追加、查找、插入、更新、删除、反转
'''
class Node(object):
    def __init__(self, data):
        self.data = data  # 节点数据域
        self.next = None  # 节点指针域
    def get_data(self):
        return self.data
class LinkList(object):
    def __init__(self, head):
        self.head = head
    # 判断当前链表是否为空
    def is_empty(self):
        return self.get_length() == 0
    # 获得当前链表的长度
    def get_length(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length
    # 链表的末尾追加一个节点
    def append_node(self, new_node):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
    # 根据节点的位置访问该节点的数据
    def find_node(self, index):
        if index < 1 or index > self.get_length():
            return print('查找节点的位置不合理！')
        node = self.head
        cur_index = 0
        while node is not None:
            cur_index += 1
            if cur_index == index:
                return node
            node = node.next
    # 根据节点的位置编号删除节点
    def delete_node(self, index):
        if index < 1 or index > self.get_length():
            return print('删除节点的位置不合理！')
        # 如果删除的是第一个元素，即head
        if index == 1:
            self.head = self.head.next
            return
        node = self.head
        cur_index = 0
        while node is not None:
            cur_index += 1
            if cur_index == index - 1:  # 找到待删除节点的前驱
                node.next = node.next.next  # 前驱节点的后置=待删除节点的后置
                return
            node = node.next
    # 根据节点的位置编号插入新节点
    def insert_node(self, index, new_node):
        if index < 1 or index > self.get_length():
            return print('插入节点的位置不合理！')
        # 如果插入的位置是第一个元素，即head
        if index == 1:
            self.head, new_node.next = new_node, self.head
            return
        node = self.head
        cur_index = 0
        while node is not None:
            cur_index += 1
            if cur_index == index - 1:  # 找到待插入节点的前驱
                # 前驱节点的后置=new_node节点，和new_node节点的后置=原前驱节点的后置
                node.next, new_node.next = new_node, node.next
                break
            node = node.next
    # 根据节点的位置编号修改节点的值
    def update_node(self, index, new_date):
        if index < 1 or index > self.get_length():
            return print('更新节点的位置不合理！')
        node = self.head
        cur_index = 0
        while node is not None:
            cur_index += 1
            if cur_index == index:
                node.data = new_date
                break
            node = node.next
    # 反转链表
    def reverse_list(self):
        p = self.head  # p指针记录当前节点
        q = p.next  # q指针表示当前节点的下一个节点，比p多走一步
        p.next = None
        while q is not None:
            temp = q.next  # 中间变量临时保存q指针的后一个节点
            q.next = p  # 改变q指针的后一个节点为p指针
            p = q  # p指针向后走一位
            q = temp  # q指针向后走一位
        self.head = p
    # 顺序输出链表
    def print_list(self):
        node = self.head
        datas = []
        while node is not None:
            datas.append(node.get_data())
            node = node.next
        return datas
if __name__ == '__main__':
    linklist = LinkList(head=Node(0))
    print('初始链表：当前链表：{}，长度为：{}'.format(linklist.print_list(), linklist.get_length()))
    [linklist.append_node(new_node=Node(data=i)) for i in range(1, 11)]
    print('追加10个元素到链表：当前链表：{}，长度为：{}'.format(linklist.print_list(), linklist.get_length()))
    '''插入操作'''
    insert_index = 3
    linklist.insert_node(index=insert_index, new_node=Node(data='insert'))
    print('插入链表第{}个位置：当前链表：{}，长度为：{}'.format(insert_index, linklist.print_list(), linklist.get_length()))
    '''查找操作'''
    find_index = 3
    find_node = linklist.find_node(index=find_index)
    print('查找链表第{}个位置：该节点值为：{}'.format(find_index, find_node.get_data()))
    '''更新操作'''
    update_index = 3
    linklist.update_node(index=update_index, new_date='update')
    print('更新链表第{}个位置：当前链表：{}，长度为：{}'.format(update_index, linklist.print_list(), linklist.get_length()))
    '''反转操作'''
    linklist.reverse_list()
    print('反转链表：{}，长度为：{}'.format(linklist.print_list(), linklist.get_length()))
    '''删除操作'''
    delete_index = 9
    linklist.delete_node(index=delete_index)
    print('删除链表第{}个位置：当前链表：{}，长度为：{}'.format(delete_index, linklist.print_list(), linklist.get_length()))
    linklist.append_node(new_node=Node(data='append'))
    print('追加链表：{}，长度为：{}'.format(linklist.print_list(), linklist.get_length()))
    '''反转操作'''
    linklist.reverse_list()
    print('反转链表：{}，长度为：{}'.format(linklist.print_list(), linklist.get_length()))