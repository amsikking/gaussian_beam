import numpy as np
from rayleigh_range import rayleigh_range
from beam_profile import beam_profile

if __name__ == "__main__":
    # Input:
    w0_um, n, lambda_um = 500, 1.0, 0.532
    # Get value:
    zr_m = rayleigh_range(w0_um, n, lambda_um)

    # Plot:
    z_m = np.linspace(-3 * zr_m, 3 * zr_m, 1000)
    wz_um = beam_profile(z_m, zr_m, w0_um)
    r_fwhm = wz_um * (2 * np.log(2))**0.5 / 2

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Gaussian beam\n (w0_um=%0.2f, n=%0.2f, lambda_um=%0.3f)'%(
        (w0_um, n, lambda_um)))
    ax.set_ylabel('Radius (um)')
    ax.set_xlabel('z (m)')
    ax.plot(z_m, wz_um, label='1/e^2', color='b')
    ax.set_ylim(ymin=0)
    plt.legend(loc="lower left")
    fig.savefig('beam_divergence.png', dpi=150)
    plt.show()
