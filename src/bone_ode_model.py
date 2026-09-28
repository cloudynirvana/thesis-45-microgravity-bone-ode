import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class BoneModelParameters:
    def __init__(self, gravity_ratio=1.0):
        # Base Komarova parameters
        self.alpha_C = 3.0
        self.beta_C = 0.2
        self.alpha_B = 0.2
        self.beta_B = 0.02
        self.g11 = 1.1
        self.g21 = 2.0
        self.g12 = 1.0
        self.g22 = 0.0
        self.k1 = 0.0748
        self.k2 = 0.0006395
        
        # Gravity parameter (1.0 = Earth, 0.0 = microgravity, 0.38 = Mars)
        self.gravity_ratio = gravity_ratio
        self.gamma_M = 0.5  # Sensitivity to mechanical unloading
        
        # Calculate steady states assuming Earth gravity
        self.C_ss = (self.beta_C / self.alpha_C)**((1 - self.g22) / (self.g11*(1-self.g22) - self.g12*self.g21)) * \
                    (self.beta_B / self.alpha_B)**(self.g21 / (self.g11*(1-self.g22) - self.g12*self.g21))
        
        self.B_ss = (self.beta_B / self.alpha_B)**((1 - self.g11) / (self.g22*(1-self.g11) - self.g12*self.g21)) * \
                    (self.beta_C / self.alpha_C)**(self.g12 / (self.g22*(1-self.g11) - self.g12*self.g21))

    def M_g(self, t):
        """Mechanical loading function."""
        return 1 + self.gamma_M * (1 - self.gravity_ratio)

def bone_ode_system(t, y, params, exercise_func, drug_func):
    C, B, Z = y
    
    # Countermeasures
    E_t = 1 + exercise_func(t)
    D_t = 1 - drug_func(t)
    
    # Avoid negative populations or zero raised to power
    C = max(1e-5, C)
    B = max(1e-5, B)
    
    dC_dt = params.alpha_C * (C**params.g11) * (B**params.g21) * params.M_g(t) * D_t - params.beta_C * C
    dB_dt = params.alpha_B * (C**params.g12) * (B**params.g22) * E_t - params.beta_B * B
    
    # Bone mass change
    dZ_dt = -params.k1 * max(0, C - params.C_ss) + params.k2 * max(0, B - params.B_ss)
    
    return [dC_dt, dB_dt, dZ_dt]

def run_simulation(duration, params, exercise=None, drug=None):
    if exercise is None:
        exercise = lambda t: 0.0
    if drug is None:
        drug = lambda t: 0.0
        
    y0 = [params.C_ss, params.B_ss, 100.0]  # Start at 100% BMD
    t_span = (0, duration)
    t_eval = np.linspace(0, duration, 1000)
    
    sol = solve_ivp(
        bone_ode_system, 
        t_span, 
        y0, 
        args=(params, exercise, drug), 
        t_eval=t_eval, 
        method='Radau'
    )
    return sol
