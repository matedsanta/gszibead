#include <iostream>
#include <string>

using namespace std;

class Human {
  private:
	string firstname = "Mate"; // Using std::string for better management
	string lastname = "Santa";

  public:
	void Speak() {
		cout << "My firstname is " << firstname << endl;
		lastname.append("s");
		cout << "My lastname is " << lastname << endl;
	}
};

struct Vec2 {
  public:
	int x;
	int y;
	void Print() { cout << "(" << x << "; " << y << ")" << endl; }
};

void Part2() {
	Vec2 pos;
	pos.x = 0;
	pos.y = 0;
	Vec2 *posptr = &pos;
	posptr->Print();

	int all = 0;
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			posptr->x = i;
			posptr->y = j;
			posptr->Print();
			all++;
		}
	}
	cout << "Number of loops: " << all << endl;
}

int main() {
	Human me;
	Human *ptr = &me;

	ptr->Speak();
	me.Speak();

	Part2(); // Calling Part2 function to demonstrate Vec2 iteration.
}
