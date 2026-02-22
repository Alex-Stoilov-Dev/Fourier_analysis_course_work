import numpy as np
import matplotlib.pyplot as plt

# Входни данни
L = 11e-3
C = 4e-6
R = 65.7

Em = 100
T = 2e-3
f = 1/T
w = 2 * np.pi * f

# Начало на проектиране на апроксимацията чрез редове на Фурие
# Времева стъпка 2ms, първите 1000 точки, двата полупериода на сигнала.
t = np.linspace(0, T, 10000) 

# Initialize the total wave as an array of zeros
e_a = np.zeros_like(t)
u_c = np.zeros_like(t)


for k in range(3):

    n = 2 * k + 1 # Number of our harmonic
    nw = n * w # Harmonic frequency
    dt = (n * w * (4*T/6))  # Фазово изместване на входния ми сигнал

    if k == 0:
        ZL1 = 1j*nw*L 
        ZC1 = -1j/(nw*C)
        Em1 = 4*Em/np.pi # Амплитуда на първия хармоник 
        initial_phase_1 = dt # Начална фаза на първия хармоник
        E_a1 = Em1/np.sqrt(2) * np.exp(1j*initial_phase_1) # Комплекс на първият хармоник на ЕДН
        Z1 = R + ZL1 # Съпротивление в RL клона
        Z2 = (ZC1 * Z1) / (ZC1 + Z1) # Съпротивление на RLC 
        Ze1 = ZL1 + Z2
        Ivhd1 = E_a1 / Ze1 # Входящ ток във веригата
        print(f"Ivhd1 value is = {Ivhd1:.3f}A\n\n")

        IRL1 = (ZC1/(ZC1 + Z1)) * Ivhd1 # Токът в клона с резистора и бобината
        IC1 = (Z1/(ZC1+Z1)) * Ivhd1 # Токът в клона с Кондензатора
        Uc1 = IC1 * ZC1
        Uc1m = np.sqrt(2) * np.abs(Uc1) # Амплитуда на Ic1
        phase_Uc1 = np.angle(Uc1) # Фаза на токът Uc1 в радиани
        phase_Uc1_deg = np.angle((Uc1)*180/np.pi)

        uC1_t = Uc1m * np.sin(nw*t + (phase_Uc1))
        plt.figure(2, figsize=(10,6))
        plt.plot(t, uC1_t, label=f'Хармоник на 1 u2 ', linestyle='--', alpha=0.5)


    if k == 1:
        ZL3 = 1j*nw*L
        ZC3 = -1j*1/(nw*C)
        Em3 = 4*Em/(n * np.pi) # Амплитуда на третия хармоник 
        initial_phase_3 = dt # Начална фаза на третия хармоник
        E_a3 = Em3/np.sqrt(2) * np.exp(1j*(initial_phase_3)) # Комплекс на третия хармоник на ЕДН
        Z1_3 = R + ZL3
        Z2_3 = (ZC3 * Z1_3) / (ZC3 + Z1_3)
        Ze1_3 = ZL3 + Z2_3
        Ivhd3 = E_a3 / Ze1_3 # Входящ ток във веригата
        print(f"Ivhd3 value is = {Ivhd3:.3f}A\n\n")
        IRL3 = (ZC3/(ZC3 + Z1_3)) * Ivhd3 # Токът в клона с резистора и бобината
        IC3 = (Z1_3/(ZC3+Z1_3)) * Ivhd3 # Токът в клона с Кондензатора
        Uc3 = IC3 * ZC3

        Uc3m = np.sqrt(2) * np.abs(Uc3) # Амплитуда на тока Uc3
        phase_Uc3 = np.angle(Uc3) # Фаза на токът Uc3 в радиани
        phase_Uc3_deg = np.angle((Uc3)*180/np.pi)  # Фаза на токът Uc3 в радиани
        uC3_t = Uc3m * np.sin(nw*t + (phase_Uc3))
        plt.figure(2, figsize=(10,6))
        plt.plot(t, uC3_t, label=f'Хармоник на 3 u2 ', linestyle='--', alpha=0.5)


    if k == 2:
        ZL5 = 1j*nw*L
        ZC5 = -1j*1/(nw*C)
        Em5 = 4*Em/(n * np.pi) # Амплитуда на петия хармоник 
        initial_phase_5 = dt # Начална фаза на петия хармоник
        E_a5 = Em5/np.sqrt(2) * np.exp(1j*initial_phase_5) # Комплекс на петия хармоник на ЕДН
        Z1_5 = R + ZL5
        Z2_5 = (ZC5 * Z1_5) / (ZC5 + Z1_5)
        Ze1_5 = ZL5 + Z2_5
        Ivhd5 = E_a5 / Ze1_5 # Входящ ток във веригата
        print(f"Ivhd5 value is = {Ivhd5:.3f}A\n\n")
        IRL5 = (ZC5/(ZC5 + Z1_5)) * Ivhd5 # Токът в клона с резистора и бобината
        IC5 = (Z1_5/(ZC5+Z1_5)) * Ivhd5 # Токът в клона с Кондензатора
        Uc5 = IC5 * ZC5

        Ir = np.sqrt(np.abs(IRL1)**2 + np.abs(IRL3)**2 + np.abs(IRL5)**2) # Ток през резистора
        Uc = np.sqrt(np.abs(Uc1)**2 + np.abs(Uc3)**2 + np.abs(Uc5)**2)
        Pr = (Ir**2) * R # Мощност на товарния резистор

        UC5m = np.sqrt(2) * np.abs(Uc5)
        phase_Uc5 = np.angle(Uc5) # Фаза на токът Uc5 в радиани
        phase_Uc5_deg = np.angle((Uc5)*180/np.pi)
        uC5_t = UC5m * np.sin(nw*t + (phase_Uc5))
        plt.figure(2, figsize=(10,6))
        plt.plot(t, uC5_t, label=f'Хармоник на 5 u2 ', linestyle='--', alpha=0.5)

        print("\n\n")

        print("--- Circuit Analysis Results (First 3 Harmonics) ---")
        
        print(f"  Кръгова честота: w={w:.3f}rad/s")

        # Harmonic 1
        print(f"Em1 = (4 * Em) / π = {Em1:.3f} V")
        print(f"ψE1 = ω * tsh = {initial_phase_1:.3f} rad")
        print(f"ψE1d = ψE1 * 180 / π = {initial_phase_1 * 180 / np.pi:.3f} deg")
        
        # Harmonic 3
        print(f"\nEm3 = (4 * Em) / (3 * π) = {Em3:.3f} V")
        print(f"ψE3 = 3 * ω * tsh = {initial_phase_3:.3f} rad")
        print(f"ψE3d = ψE3 * 180 / π = {initial_phase_3 * 180 / np.pi:.3f} deg")
        
        # Harmonic 5
        print(f"\nEm5 = (4 * Em) / (5 * π) = {Em5:.3f} V")
        print(f"ψE5 = 5 * ω * tsh = {initial_phase_5:.3f} rad")
        print(f"ψE5d = ψE5 * 180 / π = {initial_phase_5 * 180 / np.pi:.3f} deg")
        print("\n\n")

        print(f"E_a1 = {Em1:.3f}/√2 * exp(1j * {initial_phase_1:.3f}) = {E_a1.real:.3f} + {E_a1.imag:.3f}j V")
        
        # Harmonic 3
        print(f"E_a3 = {Em3:.3f}/√2 * exp(1j * {initial_phase_3:.3f}) = {E_a3.real:.3f} + {E_a3.imag:.3f}j V")
        
        # Harmonic 5
        print(f"E_a5 = {Em5:.3f}/√2 * exp(1j * {initial_phase_5:.3f}) = {E_a5.real:.3f} + {E_a5.imag:.3f}j V")
        
        # Adding Capacitor Complex Potentials (Uc)
        print("-" * 30)
        print(f"Uc1 = {np.abs(Uc1):.3f}V")
        print(f"Uc3 = {np.abs(Uc3):.3f}V")
        print(f"Uc5 = {np.abs(Uc5):.3f}V")

        print(f"Uc1 = {Uc1m:.3f}/√2 * exp(1j * {np.angle(Uc1):.3f}) = {Uc1.real:.3f} {Uc1.imag:+.3f}i V")
        print(f"Uc3 = {Uc3m:.3f}/√2 * exp(1j * {np.angle(Uc3):.3f}) = {Uc3.real:.3f} {Uc3.imag:+.3f}i V")
        print(f"Uc5 = {UC5m:.3f}/√2 * exp(1j * {np.angle(Uc5):.3f}) = {Uc5.real:.3f} {Uc5.imag:+.3f}i V")
        # Harmonic 1 (k=0) variables
        print(f"Harmonic 1 (n=1):")
        print(f"  Currents:   Ivhd={Ivhd1:.3f}A, IRL1={IRL1:.3f}A, IC1={IC1:.3f}A")
        print(f"  Phase Uc1:  {np.angle(Uc1)*180/np.pi:.3f}°")
        
        # Harmonic 3 (k=1) variables
        print(f"\nHarmonic 3 (n=3):")
        print(f"  Currents:   Ivhd={Ivhd3:.3f}A, IRL3={IRL3:.3f}A, IC3={IC3:.3f}A")
        print(f"  Phase Uc3:  {np.angle(Uc3)*180/np.pi:.3f}°")
        
        # Harmonic 5 (k=2) variables
        print(f"\nHarmonic 5 (n=5):")
        print(f"  Currents:   Ivhd={Ivhd5:.3f}A, IRL5={IRL5:.3f}A, IC5={IC5:.3f}A")
        print(f"  Phase Uc5:  {np.angle(Uc5)*180/np.pi:.3f}°")
        
        print(f"Total RMS Current through Resistor: {Ir:.3f} A")
        print(f"Power consumed by R: {Pr:.3f} W")
        print("-" * 50)

        u_c = uC1_t + uC3_t + uC5_t 
    
    harmonic = 4 * Em / (np.pi * n) * np.sin(n * w * t - dt)# Сумиране на хармониците в една финална вълна
    e_a += harmonic
    # Проектиране на всички съставящи хармоници
    plt.figure(1,figsize=(10, 6))
    plt.plot(t, harmonic, label=f'Хармоник {n}', linestyle='--', alpha=0.5)

# Графика на входното напрежение E(t)
plt.plot(t, e_a, label='Апроксимиран Сигнал', color='black', linewidth=2) # Резултатна вълна от Фурие апроксимацията
plt.plot(t, Em * np.sign(np.sin(w * t + dt)), label='Идеален Сигнал', color='red', linestyle=':', alpha=0.3) # Идеална правоъгълна вълна

plt.title('Фурие Апроксимация')
plt.xlabel('Време [ms]')
plt.ylabel('Амплитуда [V]')
plt.legend(loc='upper right', ncol=2) # ncol=2 keeps the legend tidy
plt.grid(True, alpha=0.3)

plt.figure(2)
plt.plot(t, u_c, label='Total Voltage u_c', color='black', linewidth=2)
plt.title('Графика на напрежението U2')
plt.xlabel('Време [ms]')
plt.ylabel('Амплитуда [V]')
plt.legend(loc='upper left', ncol=2)
plt.grid(True, alpha=0.3)
plt.grid(True)
plt.ticklabel_format(useOffset=False, style='plain', axis='x')
plt.show()