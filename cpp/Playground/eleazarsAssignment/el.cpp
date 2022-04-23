#include <stdio.h>
#include <iostream>
using namespace std;


//menu
void menu(){
	cout << "*********************************" << endl;
	cout << "|\tCHOOSE DIVISIBILITY\t|" << endl;
	for (size_t i = 0; i < 5; i++)
		cout << "| [" << i + 1 << "] - " 
			<< "Divisible by " << 8+i
			<< "\t\t| " << endl;
    cout << "*********************************" << endl;
}


//checker {
bool checker(int number, int div) {
	if (number % div == 0)
		return true;
	
	 else 
		return false;
}

int loop(){
	menu();

	cout << "Choose your option: ";
	int choice {};
	cin >> choice;

	cout << "Enter number: ";
	int number {};
	cin >> number;
	
	cout << boolalpha;

	switch(choice){
		case 1: cout << checker(number, 8) << endl; break;
		case 2: cout << checker(number, 9) << endl; break;
		case 3: cout << checker(number, 10) << endl; break;
		case 4: cout << checker(number, 11) << endl; break;
		case 5: cout << checker(number, 12) << endl; break;
		default: cout << "Invalid choice" << endl << loop();
	}

	cout << "Do you want to continue [Y/n]? ";
	char c {};
	cin >> c;
	if (tolower(c) == 'y')
		loop();

	return 0;
}


int main(){
	loop();

	return 0;
}