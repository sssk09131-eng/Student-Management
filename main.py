# main.py
from exam_system import ExamSystem

def main():
    system = ExamSystem()
    
    while True:
        print("\n学生信息与考场管理系统")
        print("1. 查找学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证")
        print("5. 退出")
        
        choice = input("请选择功能: ")
        
        try:
            if choice == '1':
                student_id = input("请输入学号: ")
                student = system.find_student(student_id)
                print(student)
                
            elif choice == '2':
                count = int(input("请输入点名人数: "))
                students = system.random_call(count)
                print(f"随机点名结果 ({len(students)}人):")
                for i, s in enumerate(students, 1):
                    print(f"{i}. {s.name} ({s.id})")
                    
            elif choice == '3':
                system.generate_exam_schedule()
                
            elif choice == '4':
                system.generate_exam_cards()
                
            elif choice == '5':
                print("感谢使用，再见！")
                break
                
            else:
                print("无效选择，请重新输入")
                
        except ValueError as ve:
            print(f"输入错误: {str(ve)}")
        except Exception as e:
            print(f"系统错误: {str(e)}")

if __name__ == "__main__":
    main()