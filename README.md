# Fourier Analysis

## This python script can be used to visualise fourier approximation of square waves.

Its also the solution to my Circuit Analysis course work.

## What this code does?

- It calculates the first 5 harmonics of a square wave. It solves an AC circuit analysis problem, for a nonsinusoidal wave.
- It solves the circuit, finding all of the complex impedances at the frequency of each harmonic. The code also finds the current through the load resistor, and the voltage across a capacitor.
- The code utilizes numpy for the complex calculations, and matplotlib to visualise the fourier approximations.
- Once the code solves the problem, it finds the RMS value of the current through the resistor, and the active power it consumes.
- The program plots and shows the Fourier approximation of the voltage source e_{a}(t), and the approximation of the voltage u_{2}(t). You can also compare the approximated signal to the an ideal square wave. Approximation is poor due to the small amount of harmonics used in the approximation.

