#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <ctime>

using namespace std;


int rng(){
	srand(time(NULL));
	return static_cast<int>(rand() % 1001);
}

void gameLoop(){
	bool x {true};
	int random_number {rng()}, n {0};

	while (x == true){
		cout << "Enter number: "; 	
		cin >> n;
		if (random_number == n){
			cout << "congratulations" << endl;
			break;
		} 
		
		if (random_number > n){
			cout << "higher" << endl;
			
		} else {
			cout << "lower" << endl;
		}
	}
	char c {};
	cout << "continue? [y/n]: ";
	cin >> c;
	if (tolower(c) == 'y') {
		cout << endl;
		gameLoop();
	}
}


int main(){
	gameLoop();
}
