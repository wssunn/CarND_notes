#include <string.h>
#include <iostream>

using namespace std;

class stud
{
    private:
        int num; char name[10]; char sex;
    public:
        stud(int n, const char nam[], char s)//constructor
            {num = n; strcpy_s(name, nam); sex = s;}

        //destructor
        ~stud() {cout<<"stud has been destructed!\n"<<endl;}

    void display()//成员函数，输出对象的数据
    {
        cout<<"num:"<<num<<endl;
        cout<<"name:"<<name<<endl;
        cout<<"sex:"<<sex<<endl;
    }
};

int main()
{
    // 指针对象, 不会自动调用析构，需手动释放，用delete
    stud* student1 = new stud(1, "Wang", 'f');
    student1->display();
    delete student1;

    // 临时对象（作用域：所在语句）; 作用域所在语句，执行完该语句之后被释放
    stud(2, "Hu", 'f').display();

    // 局部对象（栈区，会自动调用析构函数）
    stud stud1(3, "Wang-li", 'f'), stud2(4, "Zhang-fun", 'm');
    stud1.display(); stud2.display();
    return 0;
}
