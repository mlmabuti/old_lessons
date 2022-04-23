#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>


using namespace std;

void encrypt(){
	string alpha {"QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%&*"};
	vector <unsigned int> encrypted {};
	cout << "Enter word: ";
	string phrase {};
	cin >> phrase;
	
	//(2x+n || 2sub+pos) || sub+pos
	
	for (unsigned int pos {0}; pos < phrase.length(); pos++){
		for (unsigned int sub {0}; sub < alpha.length(); sub++){
			if (phrase[pos] == alpha[sub]){
				encrypted.push_back(pos+sub);
			}		
		}	
	}
		cout << "encrypted: " << endl;;
		for (auto i : encrypted){
			cout << i << " ";
		}
		cout << endl;
}

// write decryption here
void decrypt(){

}

int main(){

}


