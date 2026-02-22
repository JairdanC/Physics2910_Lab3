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
    slope, b = np.polyfit(x, log_y, 1) #Fit a polynomial of degree 1 (linear), slope is slope, b is y-intercept
    y_theory = slope*x + b
    y_err = (y*0.015 + 0.01) * (y**(-1)) #dy/y

    fig, ax = plt.subplots()
    plt.errorbar(x, log_y, yerr=y_err, fmt='o', color='darkblue', label='Experimental Data')
    plt.plot(x, y_theory, linewidth=2.0, linestyle='--', color='red', label='Line of Best Fit')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    ax.set_ylabel('ln(Voltage [Volts])')
    ax.set_xlabel(r'Time [$\mu$s]')

    #rescale tau to seconds
    slope = slope/1e-6
    plt.savefig('decay_log_plot.png')
    print("Experimental Tau: "  + str(-1/slope))
    print("Theoretical Tau: " + str(R*C))
    print("FIGURE SAVED")

#Task 3/4
def create_bode_plot(sig_in, sig_out_df, freq_df, type):
    #sig_in is constant
    sig_out = sig_out_df.to_numpy()
    freq = freq_df.to_numpy()
    bp_intersect = np.ones(freq.size) * -3

    gain = 20 * (np.log10(sig_out/sig_in))
    log_freq = np.log10(freq)
    if (type == "low"): 
        gain_theory = -10 * np.log10(1 + (2 *np.pi * freq * R * C)**2)
    if (type == "high"):
        gain_theory = -10 * np.log10(1 + (2 *np.pi * freq * R * C)**-2)
    gain_err = (sig_out*0.015 + 0.01) * (sig_out**(-1)) * 20 / np.log(10)

    fig, ax = plt.subplots()
    plt.errorbar(log_freq, gain, yerr=gain_err, fmt='o', color='darkblue', label='Experimental Data')
    plt.plot(log_freq, gain_theory, linewidth=2.0, linestyle='--', color='red', label='Line of Best Fit')
    plt.plot(log_freq, bp_intersect, linewidth=2.0, linestyle='--', color='grey', label='Breakpoint Gain [-3dB]')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    ax.set_ylabel('Gain [dB]')
    ax.set_xlabel('Log10(Frequency [Hz])')

    print("Theoretical Half Power Frequency: " + str(1/(2*np.pi*R*C)))
    freq_interp = np.arange(400, 550)
    log_freq_interp = np.log10(freq_interp)
    gain_interp = np.interp(log_freq_interp, log_freq, gain) #linear interpolation of the data to find a minimum, range used for around 70 plus/minus theoretical value
    bp_intersect = np.ones(gain_interp.size) * -3
    difference = np.abs(gain_interp - bp_intersect) 
    bp_exp_freq = freq_interp[np.argmin(difference)]
    print("Experimental Half Power Frequency: " + str(bp_exp_freq))
    plt.savefig(str(type) + '_pass_filter_bode_plot.png')
    print("FIGURE SAVED")

def main():
    decay_df, low_pass_df, high_pass_df = data.initialization()
    create_logy_plot(decay_df.x, decay_df.y)
    create_bode_plot(5.121, low_pass_df["V_pp (Out)"], low_pass_df["Frequency"], "low")
    create_bode_plot(5.121, high_pass_df["V_pp (Out)"], high_pass_df["Frequency"], "high")

if __name__ == "__main__":
    main()


