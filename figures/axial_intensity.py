import numpy as np
from rayleigh_range import rayleigh_range

def axial_intensity(z_m, zr_m):
    I0z = 1 / (1 + (z_m / zr_m)**2)
    if isinstance(z_m, int) or isinstance(z_m, float):
        print('Axial intensity:')
        print('(zr_m=%0.2f)'%zr_m)
        print('I0z=%0.2f'%I0z)
    return I0z

if __name__ == "__main__":
    # Input:
    w0_um, n, lambda_um = 500, 1.0, 0.532
    # Get value:
    zr_m = rayleigh_range(w0_um, n, lambda_um)
    I0z = axial_intensity(zr_m, zr_m)

    # Plot:
    z_m = np.linspace(-4 * zr_m, 4 * zr_m, 1000)
    I0z = axial_intensity(z_m, zr_m)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Gaussian beam\n (w0_um=%0.2f, n=%0.2f, lambda_um=%0.3f)'%(
        (w0_um, n, lambda_um)))
    ax.set_ylabel('Intensity (normalised)')
    ax.set_xlabel('z (m)')
    ax.plot(z_m, I0z, color='b')
    ax.axvline(x=zr_m/3, label='1/3 ZR (90%)', linestyle='--', color='g')
    ax.axvline(x=zr_m, label='1 ZR (50%)', linestyle='-.', color='r')
    ax.axvline(x=3*zr_m, label='3 ZR (10%)', linestyle=':', color='k')
    plt.legend(loc="upper left")
    fig.savefig('axial_intensity.png', dpi=150)
    plt.show()
