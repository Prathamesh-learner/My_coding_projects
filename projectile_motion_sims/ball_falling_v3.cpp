#include <iostream>
#include <raylib.h>

// Variables
double gravity = -9.80665; // meters per second squared
double ball_mass = 5.0; // kilograms
double ball_x = 20.0; // meters
double ball_y = 9.80;  // meters
double ball_vx = 0.0; // meters per second
double ball_vy = 0.0; // meters per second
double pr = 20.0;// meter to pixel ratio is 1:20
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


    ball(double a, double m, double x, double y, double vx, double vy, double height)
    {
        mass = m;
        acc = a*pr;
        bx = x*pr;
        by = height - (y*pr);
        vxb = vx*pr;
        vyb = vy*pr;
        
    }
    void drop(double dt, double et)
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

            DrawCircle(bx, by, 20, WHITE);
            t += dt;
            // bx += vxb*dt;
            vyb += acc * dt;
            by -= vyb * dt;
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
    double height = GetScreenHeight();
    double width = GetScreenWidth();
    ball bally(gravity, ball_mass, ball_x, ball_y, ball_vx, ball_vy, height);
    // objects must be created outside the game loop --> 
    while (!WindowShouldClose())
    {
        double dt = GetFrameTime();
        double et = GetTime();
        BeginDrawing();
        ClearBackground(BLACK);
        bally.drop(dt, et);
        EndDrawing();
    }
    CloseWindow();
    return 0;
}
