#include <iostream>
#include <raylib.h>

// Variables
double gravity = -9.80665; // meters per second squared
double ball_mass = 5.0; // kilograms
double ball_x = 20.0; // meters
double ball_y = 20.0; // meters
double ball_vx = 0.0; // meters per second
double ball_vy = 0.0; // meters per second
double pr = 20.0;// meter to pixel ratio is 1:20
// Screen dimensions: 800, 600 (pixels)
// Screens dimensions in meters would then be 40mx30m
// so 15 meters up should be 300 pixels from the bottom of the window would be the halfway point


// Initial RK4 setup

// Keeping the acceleration setup to account for future changes in drag
float acceleration(double a)
{
    return a;
}

struct State
{
    double x = ball_x;
    double y = ball_y;
    double vx = ball_vx;
    double vy = ball_vy;
};

State ballstate = State();

struct Derivative
{
    double dx = ball_vx;
    double dy = ball_vy;
    double dvx = 0;
    double dvy = acceleration(gravity);
};

struct ball
{
    double mass;
    double h;
    // double bx;
    // double by;
    // double vxb;
    // double vyb;
    double acc;
    double t = 0.0;

    Derivative evaluate(const State & initial, double dt, const Derivative & d)
    
    {
        State state;
        state.x = initial.x + d.dx*dt;
        state.y = initial.y + d.dy*dt;
        state.vx = initial.vx + d.dvx*dt;
        state.vy = initial.vy + d.dvy*dt;

        Derivative output;
        output.dx = state.vx;
        output.dy = state.vy;
        output.dvx = 0;
        output.dvy = acceleration(gravity);
        return output;
    }


    ball (double a, double m, double x, double y, double vx, double vy, double height)
    {
        mass = m;
        h = height;
        acc = a*pr;
        // bx = (x*pr);
        // by = h - (y*pr);//height - (y*pr);
        // vxb = vx*pr;
        // vyb = vy*pr;

    }

    void integrate(State & state, double dt, double et)
    {
        if (state.y >= 0)
        {
            std::cout << "Time: " << t << '\n';
            std::cout << "Force: " << gravity*mass << '\n';
            std::cout << "Acceleration: " << gravity << '\n';
            std::cout << "Y Velocity: " << state.vy << '\n';
            std::cout << "Y position: " << state.y << '\n';
            std::cout << "X Velocity: " << state.vx << '\n';
            std::cout << "X positiion: " << state.x << '\n';

            Derivative a,b,c,d;

            a = evaluate(state, 0.0f, Derivative());
            b = evaluate(state, dt*0.5f, a);
            c = evaluate(state, dt*0.5f, b);
            d = evaluate(state, dt, c);

            double dxdt = 1.0f/6.0f * (a.dx + 2*(b.dx + c.dx) + d.dx);
            double dydt = 1.0f/6.0f * (a.dy + 2*(b.dy + c.dy) + d.dy);
            double dvxdt = 1.0f/6.0f * (a.dvx + 2*(b.dvx + c.dvx) + d.dvx);
            double dvydt = 1.0f/6.0f * (a.dvy + 2*(b.dvy + c.dvy) + d.dvy);

            t += dt;
            state.x += dxdt*dt;
            state.y += dydt*dt;
            state.vx += dvxdt*dt;
            state.vy += dvydt*dt;

            double screen_x = state.x*pr;
            double screen_y = h - (state.y*pr);
            DrawCircle(screen_x, screen_y, 20, WHITE);
        }
        // else
        // {
        //     state.y = 0.1;
        //     state.vy = -state.vy;

        //     double screen_x = state.x*pr;
        //     double screen_y = h - (state.y*pr);

        //     DrawCircle(screen_x, screen_y, 20, WHITE);
        // }
    }

    // void drop(double dt, double et)
    // {
    //     // using conditionals for updating quantities struct functions -->
    //     if (by < 581)
    //     {
    //         std::cout << "Time: " << t << '\n';
    //         std::cout << "Force: " << acc*mass << '\n';
    //         std::cout << "Acceleration: " << acc << '\n';
    //         std::cout << "Velocity: " << vyb << '\n';
    //         std::cout << "Y position: " << by << '\n';
    //         std::cout << "X positiion: " << bx << '\n';

    //         DrawCircle(bx, by, 20, WHITE);
    //         t += dt;
    //         bx += vxb*dt;
    //         vyb += acc * dt;
    //         by -= vyb * dt;
    //     }
    //     else
    //     {
    //         by = 580;
    //         vyb = -vyb;
    //         DrawCircle(bx, by, 20, WHITE);
    //     }
    // }
};

int main()
{
    InitWindow(800, 600, "Window");
    SetTargetFPS(200);
    double height = GetScreenHeight();
    double width = GetScreenWidth();
    ball bally(gravity, ball_mass, ball_x, ball_y, ball_vx, ball_vy, height);
    // objects must be created outside the game loop so that only one is made
    while (!WindowShouldClose())
    {
        double dt = GetFrameTime();
        double et = GetTime();
        BeginDrawing();
        ClearBackground(BLACK);
        bally.integrate(ballstate, dt, et);
        // bally.drop(dt, et);
        EndDrawing();
    }
    CloseWindow();
    return 0;
}
