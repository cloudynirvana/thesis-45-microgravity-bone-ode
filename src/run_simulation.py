import numpy as np
import matplotlib.pyplot as plt
import os
from bone_ode_model import BoneModelParameters, run_simulation

def generate_figures():
    os.makedirs('plots', exist_ok=True)
    
    # Simulation Duration (Days)
    duration = 1000
    
    # --- Figure 1: Gravity Scenarios ---
    params_earth = BoneModelParameters(gravity_ratio=1.0)
    params_mars = BoneModelParameters(gravity_ratio=0.38)
    params_micro = BoneModelParameters(gravity_ratio=0.0)
    
    sol_earth = run_simulation(duration, params_earth)
    sol_mars = run_simulation(duration, params_mars)
    sol_micro = run_simulation(duration, params_micro)
    
    plt.figure(figsize=(10, 6))
    plt.plot(sol_earth.t, sol_earth.y[2], label='Earth (1g)', linewidth=2)
    plt.plot(sol_mars.t, sol_mars.y[2], label='Mars (0.38g)', linewidth=2)
    plt.plot(sol_micro.t, sol_micro.y[2], label='Microgravity (0g)', linewidth=2)
    plt.title('Figure 1: BMD Trajectories under Various Gravitational Environments')
    plt.xlabel('Time (Days)')
    plt.ylabel('Bone Mineral Density (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/Figure_1_BMD_Trajectories.png')
    plt.close()

    # --- Figure 2: Phase Portrait ---
    plt.figure(figsize=(8, 8))
    plt.plot(sol_earth.y[1], sol_earth.y[0], label='Earth Trajectory', alpha=0.7)
    plt.plot(sol_micro.y[1], sol_micro.y[0], label='Microgravity Trajectory', alpha=0.7)
    plt.scatter([params_earth.B_ss], [params_earth.C_ss], color='black', zorder=5, label='Earth Steady State')
    plt.title('Figure 2: Osteoblast-Osteoclast Dynamics Phase Portrait')
    plt.xlabel('Osteoblasts (B)')
    plt.ylabel('Osteoclasts (C)')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/Figure_2_Phase_Portrait.png')
    plt.close()
    
    # --- Figure 3: Countermeasures (Mars Transit ~ 270 days) ---
    transit_duration = 270
    
    def no_cm(t): return 0.0
    def exercise_cm(t): return 0.2  # 20% boost to formation
    def drug_cm(t): return 0.15     # 15% reduction in resorption
    
    sol_base = run_simulation(transit_duration, params_micro, no_cm, no_cm)
    sol_ex = run_simulation(transit_duration, params_micro, exercise_cm, no_cm)
    sol_drug = run_simulation(transit_duration, params_micro, no_cm, drug_cm)
    sol_combo = run_simulation(transit_duration, params_micro, exercise_cm, drug_cm)
    
    bmd_final = [
        sol_base.y[2][-1],
        sol_ex.y[2][-1],
        sol_drug.y[2][-1],
        sol_combo.y[2][-1]
    ]
    labels = ['No CM', 'Exercise', 'Bisphosphonates', 'Combined']
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, bmd_final, color=['red', 'orange', 'blue', 'green'])
    plt.axhline(y=100, color='black', linestyle='--', label='Baseline BMD (100%)')
    plt.title('Figure 3: Comparison of Countermeasure Strategies after 9-Month Mars Transit')
    plt.ylabel('Final Bone Mineral Density (%)')
    plt.ylim(80, 105)
    plt.legend()
    for i, v in enumerate(bmd_final):
        plt.text(i, v + 0.5, f"{v:.1f}%", ha='center')
    plt.savefig('plots/Figure_3_Countermeasures.png')
    plt.close()

if __name__ == "__main__":
    print("Running simulations and generating figures...")
    generate_figures()
    print("Figures saved in 'plots' directory.")
