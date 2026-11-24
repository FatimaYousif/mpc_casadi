# MPC Controller Using CasADi

A simple Model Predictive Control (MPC) node for a differential-drive robot, built with [CasADi](https://web.casadi.org/) and [IPOPT](https://coin-or.github.io/Ipopt/). The node reads the robot's pose and a goal pose, solves a nonlinear optimization problem at every step, and publishes velocity commands to drive the robot to the goal.

## Features

- Unicycle (differential-drive) model with Euler discretization
- Receding-horizon MPC solved with IPOPT (20 steps, 0.1 s time step)
- Velocity limits on linear and angular speed
- Optional circular obstacle avoidance constraints
- Publishes the predicted local path for visualization (e.g. in RViz)
- Stops automatically when the goal is reached

## How it works

**State:** `[x, y, theta]`  **Control:** `[v, omega]`

At each control cycle (10 Hz), the node:

1. Builds an initial guess by interpolating from the current state to the goal.
2. Solves the NLP, minimizing distance to the goal plus a control effort penalty, subject to the dynamics, input bounds, and obstacle constraints.
3. Publishes the first control input as a `Twist` message.
4. Publishes the full predicted trajectory as a `Path`.
