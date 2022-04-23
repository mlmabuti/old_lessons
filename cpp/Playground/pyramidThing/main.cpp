#include <iostream>
#include <string>

using namespace std;


int main(){
	string userInput;

	cout << "Enter a string: ";
	cin >> userInput;

	size_t size = userInput.length();

	for (size_t i {0}; i < size; i++){
		for (size_t j {size-i}; j > 0; j--){
			cout << " ";
		}

		for (size_t k {0}; k <= i; k++){
			cout << userInput[k];
		}

		for (size_t l = i; l > 0; l--){
			cout << userInput[l-1];
		}	
		cout << endl;
	}
}
