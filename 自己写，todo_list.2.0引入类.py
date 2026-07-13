import sys
import time
def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

class TodoList:
    def __init__(self):
        self.todo_list=[]

    def checking_list(self):
        if not self.todo_list:
            typing("待办现在为空！")
        else:
            typing("待办如下：")           
            for index,item in enumerate(self.todo_list,1):
                typing(f"{index}. {item}")
    
    def add_list(self,task):
        if not task:
            typing("输入不能为空！")
        else:
            self.todo_list.append(task)
            typing(f"已添加待办：'{task}'!")
    
    def delete_list(self,delete_task):
        if not self.todo_list:
            typing("现在待办为空")
            return
        try:
            if 0<=int(delete_task)-1<len(self.todo_list):
                removed=self.todo_list.pop(int(delete_task)-1)
                typing(f"已删除待办：'{removed}'!")
            else:
                typing("输入无效，请输入正确范围内的数字编号!")
        except ValueError:
            typing("输入无效，请输入有效的数字编号!")

def main():
    manager=TodoList()
    
    while True:
        typing("欢迎使用待办事项管理器！")
        choice=input("请输入任务编号：[1]查看待办，[2]添加待办，[3]删减待办，[4]退出待办：").strip()
        if choice=="1":
            manager.checking_list()
        elif choice=="2":
            task=input("输入你要添加的待办：")
            manager.add_list(task)
        elif choice=="3":
            delete_task=input("请输入要删减的待办编号：")
            manager.delete_list(delete_task)
        elif choice=="4":
            typing("那么再见啦！")
            break
        else:
            typing("请输入1至4的数字!")

if __name__=="__main__":
    main()
