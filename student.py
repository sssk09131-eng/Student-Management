# student.py
class Student:
    """
    学生数据类，用于存储学生信息
    """
    def __init__(self, id, name, gender, class_name, college):
        """
        初始化学生对象
        :param id: 学号
        :param name: 姓名
        :param gender: 性别
        :param class_name: 班级
        :param college: 学院
        """
        self.id = id
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.college = college
    
    def __str__(self):
        """
        重写__str__方法，提供友好打印格式
        :return: 格式化的学生信息字符串
        """
        return f"学号: {self.id}, 姓名: {self.name}, 性别: {self.gender}, 班级: {self.class_name}, 学院: {self.college}"