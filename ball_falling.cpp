#include <iostream>

// Constants
double gravity = 9.80665; // meters per second squared
double ball_mass = 5.0; // kilograms
double ball_x = 0.0; // meters
double ball_y = 15.0;  // meters
double ball_vx = 0.0; // meters per second
double ball_vy = 0.0; // meters per second

struct ball
{
    double mass;
    double bx;
    double by;
    double acc;
    double vxb;
    double vyb;
    double t = 0.0;
    double dt;


    ball(double a, double m, double x, double y, double vx, double vy)
    {
        mass = m;
        acc = a;        
        bx = x;
        by = y;
        vxb = vx;
        vyb = vy;
        dt = 0.01;
    }
    void drop ()
    {
        while (by > 0)
        {
            std::cout << "Time: " << t << '\n';
            std::cout << "Force: " << acc*mass << '\n';
            std::cout << "Acceleration: " << acc << '\n';
            std::cout << "Velocity: " << vyb << '\n';
            std::cout << "X position: " << by << '\n';
            t += dt;
            vyb += acc*dt;
            by -= vyb*dt;   
        }

    }
};

int main()
{
    ball bally(gravity, ball_mass, ball_x, ball_y, ball_vx, ball_vy);
    bally.drop();
};