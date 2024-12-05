import numpy as np
from statsmodels.stats.power import TTestIndPower
import matplotlib.pyplot as plt

def perform_power_analysis(effect_size=0.2, alpha=0.05, power=0.8):
    """
    Perform a power analysis to calculate the required sample size.
    
    Parameters:
    - effect_size (float): The standardized effect size (Cohen's d).
    - alpha (float): The significance level (default is 0.05).
    - power (float): The desired power (default is 0.8).

    Returns:
    - sample_size (int): The calculated required sample size.
    """
    analysis = TTestIndPower()

    sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

    print(f"Required sample size for effect size {effect_size}, alpha {alpha}, and power {power}: {int(np.ceil(sample_size))}")
    return int(np.ceil(sample_size))

def plot_power_curve(effect_sizes, alpha=0.05, power=0.8):
    """
    Plot a power curve for a range of effect sizes.

    Parameters:
    - effect_sizes (list): A list of effect sizes (Cohen's d) to evaluate.
    - alpha (float): The significance level (default is 0.05).
    - power (float): The desired power (default is 0.8).
    """
    analysis = TTestIndPower()

    sample_sizes = [analysis.solve_power(effect_size=es, alpha=alpha, power=power, alternative='two-sided') for es in effect_sizes]

    plt.figure(figsize=(8, 6))
    plt.plot(effect_sizes, sample_sizes, marker='o', linestyle='-', color='b')
    plt.title('Power Curve: Sample Size vs. Effect Size')
    plt.xlabel('Effect Size (Cohen\'s d)')
    plt.ylabel('Sample Size')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Parameters for power analysis
    default_effect_size = 0.5
    default_alpha = 0.05
    default_power = 0.8

    # Perform power analysis
    required_sample_size = perform_power_analysis(effect_size=default_effect_size, alpha=default_alpha, power=default_power)

    # Plot power curve for a range of effect sizes
    effect_size_range = np.linspace(0.1, 0.5, 10)  # Range of effect sizes from 0.1 to 0.5
    plot_power_curve(effect_size_range, alpha=default_alpha, power=default_power)
