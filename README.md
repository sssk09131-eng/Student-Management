# 詹泽林-25365030-第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略

步骤1：确定需要生成的模块有两部分：student类和examsystem类，而需要实现的功能有4个，依次进行。
步骤2：在student.py文件中让AI定义两个函数：Student和str，保证学生信息的提取和后面的输出
实现信息初始化功能，保证输出。
步骤3：让AI实现信息初始化功能，在exam_system中借助步骤二定义的Student函数获取并初始化学生姓名、学号等信息。
步骤4：让AI实现随机点名功能，我添加了非数字异常处理。
步骤4：让AI实现考场安排表生成，我调整了时间格式，并确保文件第一行包含生成时间，符合要求。
步骤5：让AI实现准考证生成


## 2. 核心 Prompt 迭代记录

初始 Prompt：请用Python写一个学生信息管理系统，要求包含查找、随机点名、生成考场安排表。

AI 生成的问题/缺陷：
- 没有使用面向对象编程
- 没有处理异常
- 考场安排表里面没有包含生成时间
- 使用了第三方库

优化后的 Prompt (追问)：
请用Python面向对象编程实现学生信息管理系统，必须包含Student类和ExamSystem类，
需要满足以下要求
1.处理所有异常
2.仅能使用标准库
3.考场安排表第一行必须包含生成时间。

## 3. Debug 与异常处理记录

报错类型/漏洞现象：学生名单获取失败。原因是给ai的要求中，学生名单的文件：人工智能编程语言学生名单.txt,但是我自己新建文件的时候写的是student.txt，所以函数没法获取学生名单

解决过程：
- 修改str的文件名为“student.txt”


## 4. 人工代码审查

def _load_students(self, filename: str) -> Dict[str, Student]:
    
   
    #param filename: 学生名单文件路径
    #return: 学生字典，以学号为键
    
    students = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 跳过标题行
            next(f)
            for line in f:
                data = line.strip().split()
                if len(data) == 6:  # 确保数据行长度为6，即有且仅包含6个字段
                    # 从学生名单文件中的格式来看，数据顺序为：序号 姓名 性别 班级 学号 学院
                    id = data[4]  # 学号是第5个字段（索引4）
                    name = data[1]  # 姓名是第2个字段（索引1）
                    gender = data[2]  # 性别是第3个字段（索引2）
                    class_name = data[3]  # 班级是第4个字段（索引3）
                    college = data[5]  # 学院是第6个字段（索引5）
                    students[id] = Student(id, name, gender, class_name, college)
        return students
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在，请检查路径")
        return {}
    except Exception as e:
        print(f"加载学生名单时出错: {str(e)}")
        return {}
