

#include <iostream>
using namespace std;

class Date
{
public:
    //constructor function
    int year;
    Date(){year = 2000; date = 5;}

    //this pointer makes it clear that Date->year = year (variable)
    //      rather than year(variable) = year(variable)
    Date(int year, int date){this->year = year; this->date = date;}

    //destructor function
    virtual ~Date(){cout << "  Date is destructed" << endl;}

    // function
    void Display(){cout << "\nyear " << year << endl;}
    void SetYear(int year){this->year = year;}

    void display_and_show(Date date1, int year){cout << date1.year << " " << year;}
    //*this pointer is used to pass this Date class itself
    void disp_this(){display_and_show(*this, 123456);}

private:
    int date;
};

int main()
{
    Date firstDate;
    firstDate.SetYear(2018);
    firstDate.Display();
    firstDate.disp_this();
    return 0;
}

