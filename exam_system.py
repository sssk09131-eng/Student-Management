# exam_system.py
import os
import random
import time
from typing import Dict, List
from student import Student

class ExamSystem:
    """
    学生信息与考场管理系统核心逻辑
    """
    def __init__(self, filename: str = "student.txt"):
        """
        初始化系统，加载学生名单
        :param filename: 学生名单文件路径
        """
        self.students: Dict[str, Student] = self._load_students(filename)
    
    def _load_students(self, filename: str) -> Dict[str, Student]:
        """
        私有方法：加载学生名单文件
        :param filename: 学生名单文件路径
        :return: 学生字典，以学号为键
        """
        students = {}
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                # 跳过标题行
                next(f)
                for line in f:
                    data = line.strip().split()
                    # 确保数据行包含5个字段（序号、姓名、性别、班级、学号、学院）
                    if len(data) == 6:
                        # 从文件格式看，数据顺序为：序号 姓名 性别 班级 学号 学院
                        # 提取所需字段：学号(第5个)、姓名(第2个)、性别(第3个)、班级(第4个)、学院(第6个)
                        id = data[4]
                        name = data[1]
                        gender = data[2]
                        class_name = data[3]
                        college = data[5]
                        students[id] = Student(id, name, gender, class_name, college)
            return students
        except FileNotFoundError:
            print(f"错误：文件 {filename} 不存在，请检查路径")
            return {}
        except Exception as e:
            print(f"加载学生名单时出错: {str(e)}")
            return {}
    
    def find_student(self, student_id: str) -> Student:
        """
        查找学生信息
        :param student_id: 学号
        :return: 学生对象
        """
        if student_id in self.students:
            return self.students[student_id]
        else:
            raise ValueError(f"学号 {student_id} 不存在，请检查输入")
    
    def random_call(self, count: int) -> List[Student]:
        """
        随机点名功能
        :param count: 点名数量
        :return: 随机学生列表
        """
        if not isinstance(count, int) or count <= 0:
            raise ValueError("点名数量必须是正整数")
        if count > len(self.students):
            raise ValueError(f"点名数量不能超过总人数 {len(self.students)}")
        
        # 使用random.sample确保不重复
        student_ids = random.sample(list(self.students.keys()), count)
        return [self.students[uid] for uid in student_ids]
    
    @staticmethod
    def get_current_time() -> str:
        """
        静态方法：获取当前时间（用于考场安排表）
        :return: 格式化的时间字符串
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    def generate_exam_schedule(self, output_file: str = "考场安排表.txt") -> None:
        """
        生成考场安排表
        :param output_file: 输出文件名
        """
        try:
            # 随机打乱学生顺序
            student_list = list(self.students.values())
            random.shuffle(student_list)
            
            # 生成时间
            timestamp = self.get_current_time()
            
            # 写入文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"生成时间：{timestamp}\n")
                for idx, student in enumerate(student_list, 1):
                    f.write(f"{idx},{student.name},{student.id}\n")
            print(f"考场安排表已生成：{output_file}")
        except Exception as e:
            print(f"生成考场安排表时出错: {str(e)}")
    
    def generate_exam_cards(self, output_dir: str = "准考证") -> None:
        """
        生成准考证
        :param output_dir: 准考证文件夹名
        """
        try:
            # 创建文件夹
            os.makedirs(output_dir, exist_ok=True)
            
            # 随机打乱学生顺序
            student_list = list(self.students.values())
            random.shuffle(student_list)
            
            # 生成准考证
            for idx, student in enumerate(student_list, 1):
                card_file = os.path.join(output_dir, f"{idx:02d}.txt")
                with open(card_file, 'w', encoding='utf-8') as f:
                    f.write(f"座位号: {idx}\n")
                    f.write(f"姓名: {student.name}\n")
                    f.write(f"学号: {student.id}\n")
            print(f"准考证已生成到 {output_dir} 文件夹")
        except Exception as e:
            print(f"生成准考证时出错: {str(e)}")