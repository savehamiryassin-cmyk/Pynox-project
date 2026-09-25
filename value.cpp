#include <iostream>
using namespace std;
int main()
{
	float Pynox_version = 1.0;
	int build_number = 20;
	bool activate = true;
	char info = 'cpu 13th';
	cout << sizeof(Pynox_version) << endl;
	cout << sizeof(build_number) << endl;
	cout << sizeof(activate) << endl;
	cout << sizeof(info) << endl;
	int architector;
	cout << "Enter architector(only num):";
	cin >> architector;
	if(architector == 64){
		bool platform = true;
		cout << "your system compatible for Pynox"
		
	}
	else if(architector == 32){
		bool platform = false;
		cout << "your system not compatible";
	}
	else{
		cout << "Try again later";
	}
	
	
	
}
