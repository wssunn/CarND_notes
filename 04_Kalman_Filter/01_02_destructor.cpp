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

    void display()//��Ա������������������
    {
        cout<<"num:"<<num<<endl;
        cout<<"name:"<<name<<endl;
        cout<<"sex:"<<sex<<endl;
    }
};

int main()
{
    // ָ�����, �����Զ��������������ֶ��ͷţ���delete
    stud* student1 = new stud(1, "Wang", 'f');
    student1->display();
    delete student1;

    // ��ʱ����������������䣩; ������������䣬ִ��������֮���ͷ�
    stud(2, "Hu", 'f').display();

    // �ֲ�����ջ�������Զ���������������
    stud stud1(3, "Wang-li", 'f'), stud2(4, "Zhang-fun", 'm');
    stud1.display(); stud2.display();
    return 0;
}
