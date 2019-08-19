
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
	int i = 30;

	int *pi = &i;
  	int **ppi = &pi;
	std::cout << "*pi = " << *pi << std::endl;       //一级指针
  	std::cout << "pi = " << pi << std::endl;
	std::cout << "**ppi = " << **ppi << std::endl; //二级指针
	std::cout << "i = " << i <<std::endl;

	*pi = 20;
 	std::cout << "\nchange *pi" << std::endl;
	std::cout << "*pi = " << *pi << std::endl;  //改变一级指针值
	std::cout << "pi = " << pi << std::endl;
  	std::cout << "**ppi = " << **ppi <<std::endl;
  	std::cout << "i = " << i <<std::endl;

	int b = 10;
	*ppi = &b;
  	std::cout << "\nchange **ppi" << std::endl;
	std::cout << "*pi = " << *pi << std::endl;  //改变一级指针的指向
	std::cout << "pi = " << pi << std::endl;
	std::cout << "**ppi = " << **ppi << std::endl;
  	std::cout << "i = " << i <<std::endl;

	system("pause");
	return 0;
}
