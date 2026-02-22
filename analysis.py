import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

R = 3300 #ohms
C = 1e-7 #farads 100nF

#Task 2: 
def create_logy_plot(df_x, df_y):
    x = df_x.to_numpy()
    y = df_y.to_numpy()

    log_y = np.log(y)
    slope, b = np.polyfit(x, log_y, 1) #Fit a polynomial of degree 1 (linear), tau is slope, b is y-intercept
    y_theory = slope*x + b
    y_err = (y*0.015 + 0.01) * (y**(-1)) #dy/y

    fig, ax = plt.subplots()
    plt.errorbar(x, log_y, yerr=y_err, fmt='o', color='darkblue', label='Experimental Data')
    plt.plot(x, y_theory, linewidth=2.0, color='orange', label='Line of Best Fit')
    ax.grid(True, linestyle=':', alpha=0.4)
    plt.savefig('decay_log_plot.png')
    print("Tau: "  + str(-1/slope))
    print("FIGURE SAVED")

#Task 3/4
def create_bode_plot(sig_in, sig_out_df, freq_df, type):
    #sig_in is constant
    sig_out = sig_out_df.to_numpy()
    freq = freq_df.to_numpy()

    gain = 20 * (np.log10(sig_out/sig_in))
    log_freq = np.log10(freq)
    if (type == "low"): 
        gain_theory = -10 * np.log10(1 + (2 *np.pi * freq * R * C)**2)
    if (type == "high"):
        gain_theory = -10 * np.log10(1 + (2 *np.pi * freq * R * C)**-2)
    gain_err = (sig_out*0.015 + 0.01) * (sig_out**(-1)) * 20 / np.log(10)

    fig, ax = plt.subplots()
    plt.errorbar(log_freq, gain, yerr=gain_err, fmt='o', color='darkblue', label='Experimental Data')
    plt.plot(log_freq, gain_theory, linewidth=2.0, color='orange', label='Line of Best Fit')
    ax.grid(True, linestyle=':', alpha=0.4)
    plt.savefig(str(type) + '_pass_filter_bode_plot.png')
    print("FIGURE SAVED")

def main():
    decay_df, low_pass_df, high_pass_df = data.initialization()
    create_logy_plot(decay_df.x, decay_df.y)
    create_bode_plot(5.121, low_pass_df["V_pp (Out)"], low_pass_df["Frequency"], "low")
    create_bode_plot(5.121, high_pass_df["V_pp (Out)"], high_pass_df["Frequency"], "high")

if __name__ == "__main__":
    main()


