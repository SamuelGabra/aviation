# Aviation

Simple model of global aviation

## Model description

The model describes the number of passengers per flight using _two_ equations and a set of variables and constants.

## Variables

The list of variables is described in the table below:

| Variable name            | Description                                                                    | Type    | Value     | Reference               |
| ------------------------ | ------------------------------------------------------------------------------ | ------- | --------- | ----------------------- |
| $seats_{aircraft}$       | number of seats per aircraft                                                   | Input   | 200       |                         |
| $passengers_{year}$      | number of commercial aviation passengers per year                              | Input   | 6 x 10^9^ |                         |
| $aircraftflights_{day}$  | number of aircraft flights per day                                             | Input   | 3         | OAG[@oag2025statistics] |
| $passengers_{day}$       | number of passengers flying per day                                            | Derived | 2         |                         |
| $aircraftfleet_{global}$ | Global aircraft fleet required to transport the specified number of passengers | Derived |           |                         |

## Constants

These are the model parameters that are not expected to change by the users

| Constant name | Description             | Value  | Reference |
| ------------- | ----------------------- | ------ | --------- |
| $days_{year}$ | number of days per year | 365.25 | --        |

## Equations

The total number of aviation passengers travelling per day is described using equation $\ref{eq:globalpassengers}$, while the total number of global aircraft fleet is decribed in equation $\ref{eq:aircraftfleet}$.

$$
\begin{equation}
    passengers_{day} = \frac{passengers_{year}}{days_{year}}
    \label{eq:globalpassengers}
\end{equation}
$$

$$
\begin{equation}
    aircraftfleet_{global} = \frac{passengers_{day}}{days_{year} * aircraftflights_{day}}
    \label{eq:aircraftfleet}
\end{equation}
$$

## References
