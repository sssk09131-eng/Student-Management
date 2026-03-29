# 张三-2001101-第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略

步骤1：先让AI生成Student类和ExamSystem类的基本框架，确保符合OOP规范。
步骤2：让AI实现信息初始化功能，我添加了文件路径处理和异常处理。
步骤3：让AI实现随机点名功能，我添加了输入验证和非数字异常处理。
步骤4：让AI实现考场安排表生成，我调整了时间格式并确保文件第一行包含生成时间。
步骤5：让AI实现准考证生成，我添加了文件夹创建逻辑和文件名格式化。

## 2. 核心 Prompt 迭代记录

初代 Prompt：请用Python写一个学生信息管理系统，要求包含查找、随机点名、生成考场安排表。

AI 生成的问题/缺陷：
- 没有使用面向对象编程
- 没有处理异常
- 文件路径硬编码
- 没有包含生成时间

优化后的 Prompt (追问)：
请用Python面向对象编程实现学生信息管理系统，必须包含Student类和ExamSystem类，处理所有异常，使用标准库，文件路径可配置，考场安排表第一行必须包含生成时间。

## 3. Debug 与异常处理记录

报错类型/漏洞现象：文件解析错误，由于学生名单格式不匹配。

解决过程：
- 分析了学生名单文件的格式
- 修改了文件解析逻辑，确保正确提取学号、姓名等信息
- 添加了对文件格式的检查，避免解析错误

最终修改：
- 在_load_students方法中，修改了数据提取逻辑
- 添加了对文件格式的检查，确保只处理包含6个字段的行

## 4. 人工代码审查

```python
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
                if len(data) == 6:  # 确保数据行包含6个字段
                    # 从文件格式看，数据顺序为：序号 姓名 性别 班级 学号 学院
                    id = data[4]  # 学号是第5个字段（索引4）
                    name = data[1]  # 姓名是第2个字段（索引1）
                    gender = data[2]  # 性别是第3个字段（索引2）
                    class_name = data[3]  # 班级是第4个字段（索引3）
                    college = data[5]  # 学院是第6个字段（索引5）
                    students[id] = Student(id, name, gender, class_name, college)
        return students
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在，请检查路径")
        return {}
    except Exception as e:
        print(f"加载学生名单时出错: {str(e)}")
        return {}