#include <iostream>
#include <raylib.h>

// Variables
double gravity = -9.80665; // meters per second squared
double ball_mass = 5.0; // kilograms
double ball_x = 20.0; // meters
double ball_y = 15.0;  // meters
double ball_vx = 0.0; // meters per second
double ball_vy = 0.0; // meters per second
double c = 20.0;// meter to pixel ratio is 1:20
// Screens dimensions in meters would then be 40mx30m
// so 15 meters up should be 300 pixels from the bottom of the window here which is 300

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
        bx = x*c;
        by = y*c;
        vxb = vx*c;
        vyb = vy*c;
        dt = 0.01;
    }
    void drop()
    {
        // use conditionals for position updating struct functions -->
        if (by < 580)
        {
            std::cout << "Time: " << t << '\n';
            std::cout << "Force: " << acc*mass << '\n';
            std::cout << "Acceleration: " << acc << '\n';
            std::cout << "Velocity: " << vyb << '\n';
            std::cout << "Y position: " << by << '\n';
            std::cout << "X positiion: " << bx << '\n';
            if (by > 580)
            {
                by = 580;
            }
            DrawCircle(bx, by, 20, WHITE);
            t += dt;

            // bx += vxb*dt;

            vyb += acc;
            by -= vyb;
        }
        else
        {
            by = 580;
            DrawCircle(bx, by, 20, WHITE);
        }

    }
};

int main()
{
    InitWindow(800, 600, "Window");
    SetTargetFPS(60);
    // objects must be created outside the game loop --> 
    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);
        ball bally(gravity, ball_mass, ball_x, ball_y, ball_vx, ball_vy);
        bally.drop();
        EndDrawing();
    }
    CloseWindow();
    return 0;
}
