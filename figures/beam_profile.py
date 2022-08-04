import numpy as np
from rayleigh_range import rayleigh_range

def beam_profile(z_m, zr_m, w0_um):
    wz_um = w0_um * (1 + (z_m / zr_m)**2)**0.5
    return wz_um

if __name__ == "__main__":
    # Input:
    w0_um, n, lambda_um = 500, 1.0, 0.532
    # Get value:
    zr_m = rayleigh_range(w0_um, n, lambda_um)

    # Plot:
    z_m = np.linspace(-zr_m, zr_m, 1000)
    wz_um = beam_profile(z_m, zr_m, w0_um)
    r_fwhm = wz_um * (2 * np.log(2))**0.5 / 2

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Gaussian beam\n (w0_um=%0.2f, n=%0.2f, lambda_um=%0.3f)'%(
        (w0_um, n, lambda_um)))
    ax.set_ylabel('Radius (um)')
    ax.set_xlabel('z (m)')
    ax.plot(z_m, wz_um, label='w(z) (1/e^2)', color='b')
    ax.plot(z_m, r_fwhm, label='FWHM(z)', linestyle=':', color='b')
    ax.axvline(x=zr_m/3, label='1/3 ZR (90%I0)', linestyle='--', color='g')
    ax.axvline(x=zr_m, label='1 ZR (50%I0)', linestyle='-.', color='r')
    ax.set_ylim(ymin=0)
    plt.legend(loc="lower left")
    fig.savefig('beam_profile.png', dpi=150)
    plt.show()
