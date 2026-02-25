# Fourier Analysis

## This python script can be used to visualise fourier approximation of square waves.

Its also the solution to my Circuit Analysis course work.

## What this code does?

- It calculates the first 5 harmonics of a square wave. It solves an AC circuit analysis problem, for a nonsinusoidal wave.
- It solves the circuit, finding all of the complex impedances at the frequency of each harmonic. The code also finds the current through the load resistor, and the voltage across a capacitor.
- The code utilizes numpy for the complex calculations, and matplotlib to visualise the fourier approximations.
- Once the code solves the problem, it finds the RMS value of the current through the resistor, and the active power it consumes.
- The program plots and shows the Fourier approximation of the voltage source $e_{A}(t)$, and the approximation of the voltage $u_{2}(t)$. You can also compare the approximated signal to the an ideal square wave. Approximation is poor due to the small amount of harmonics used in the approximation.

## AC Circuit to solve
![alt text](https://github.com/Alex-Stoilov-Dev/Fourier_analysis_course_work/blob/main/Circuit.png)

## Signal Type
![alt text](https://github.com/Alex-Stoilov-Dev/Fourier_analysis_course_work/blob/main/Initial%20Signal.png)

## Approximation function for our signal
![alt text](https://github.com/Alex-Stoilov-Dev/Fourier_analysis_course_work/blob/main/Approximation%20function.png)

## Graph of fourier approximation of the voltage source $e_{A}(t)$
![alt text](https://github.com/Alex-Stoilov-Dev/Fourier_analysis_course_work/blob/main/Plot%20of%20the%20fourier%20approximation%20of%20the%20voltage%20source.png)

## Graph of fourier approximation of the voltage across the capacitor $u_{2}(t)$
![alt text](https://github.com/Alex-Stoilov-Dev/Fourier_analysis_course_work/blob/main/Plot%20of%20u2%20voltage.png)

## Note
- Running the code you will also get quite a lot of information as terminal output. That information is all relevant to my course work. The reason it is in the last "if" statement is because python would throw errors otherwise. This code is published so I can keep track of it and pull it if I need to make any changes when submitting my work. As such it has high specificity to the my specific circuit analysis problem. It can be reused, as long as the circuit is of the same type (meaning it has the same amount of elements and they are arranged in the same way), and your initial       signal is a square wave (with the same offset, which if not can be adjusted). You may have to adjust the Constant values at the start of the file if your problem has different values. You can adjust the range of the for-loop, which will provide you with a graphic of a fourier approximation of the voltage source $e_{A}(t)$ with more harmonics. More harmonics means a better approximation, and it's pretty cool to see at k = 50, or even k = 100, how close we can get to an almost ideal square wave.
  
