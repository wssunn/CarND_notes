#include <iostream>
#include <vector>

using namespace std;

struct Particle{double x;double y;};

int main(){
    vector<int> myvector = {1,2,3,4,5,6,7,8,9,10};

    int *k = &myvector[3];
    *k = 0;
    cout << k << endl;

    for (auto &i : myvector){
        cout << i << " ";
        i = 10;
    }
    cout << endl;

    for (auto &i : myvector){cout << i << " ";}
    cout << endl;

    vector<Particle> particles;
    Particle p;
    p.x = 10.0, p.y = 5.0;

    particles.push_back(p);
    particles.push_back(p);

    for (size_t i=0; i < particles.size(); ++i){
        Particle *a = &particles[i];
        a->x = 300;
        cout << a->x << " " << a->y << endl;
    }
    for (auto &p : particles){   
        cout << p.x << " " << p.y << endl;
        p.x = 100;
    }
    for (auto &p : particles)
    {cout << p.x << " " << p.y << endl;}

    double a = 10*
                5;
    cout << a << endl;

    int b = int(10.4); cout << b << endl;

    return 0;
}