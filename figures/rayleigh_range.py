import numpy as np

def rayleigh_range(w0_um, n, lambda_um):
    paraxial_limit_um = (3 * lambda_um) / (2 * np.pi * n) # P. Vaveliuk 2007
    zr_m = 1e-6 * (np.pi * w0_um**2 * n / lambda_um)
    if isinstance(w0_um, int) or isinstance(w0_um, float):
        print('Rayleigh range:')
        print('(w0_um=%0.2f, n=%0.2f, lambda_um=%0.2f)'%(w0_um, n, lambda_um))
        print('paraxial_limit_um=%0.2f'%paraxial_limit_um)
        print('zr_m=%0.2f'%zr_m)
        assert w0_um >= paraxial_limit_um, 'beam waist too small'
    else:
        assert min(w0_um) >= paraxial_limit_um, 'beam waist too small'
    return zr_m

if __name__ == "__main__":
    # Input:
    w0_um, n, lambda_um = 500, 1.0, 0.532

    # Get value:
    zr_m = rayleigh_range(w0_um, n, lambda_um)

    # Plot:
    w0_um = np.linspace(100, 1000, 1000)
    zr_m = rayleigh_range(w0_um, n, lambda_um)
    diameter_mm = 1e-3 * 2 * w0_um

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Gaussian beam\n (n=%0.2f, lambda_um=%0.3f)'%((n, lambda_um)))
    ax.set_ylabel('Rayleigh range (m)')
    ax.set_xlabel('Beam diameter (mm)')
    ax.plot(diameter_mm, zr_m, color='b')
    ax.axvline(x=1, label='1mm beam', linestyle='--', color='r')
    plt.legend(loc="upper left")
    fig.savefig('rayleigh_range.png', dpi=150)
    plt.show()
