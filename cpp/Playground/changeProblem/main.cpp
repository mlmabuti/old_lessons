#include <iostream>

using namespace std;
int main(){
	const int dollar {100}, quarter {25}, dime {10}, nickel {5}, penny {1};
	int bal {}, dollars {}, quarters {}, dimes {}, nickels {}, pennies {};
	
	cout << "Enter value:" ;
	cin >> bal;

	dollars = bal/dollar;
	bal %= dollar;

	quarters = bal/quarter;
	bal %= quarter;

	dimes = bal/dime;
	bal %= dime;

	nickels = bal/nickel;
	bal %= nickel;

	pennies = bal/penny;
	bal %= penny;
	
	cout << dollars << endl << quarters << endl
		<< dimes << endl << nickels << endl
		<< pennies << endl;

	return 0;
}
