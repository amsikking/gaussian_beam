import numpy as np
from rayleigh_range import rayleigh_range

def intensity(r_um, z_m, zr_m, w0_um):
    r_m = 1e-6 * r_um
    w0_m = 1e-6 * w0_um
    wz_m = w0_m * (1 + (z_m / zr_m)**2)**0.5
    Irz = (w0_m / wz_m)**2 * np.exp(-2 * (r_m / wz_m)**2)
    if isinstance(r_m, int) or isinstance(r_m, float):
        print('Intensity:')
        print('(w0_um=%0.2f, zr_m=%0.2f, z_m=%0.2f, r_m=%0.2f)'%(
            w0_um, zr_m, z_m, r_m))
        print('Irz=%0.2f'%Irz)
    return Irz

if __name__ == "__main__":
    # Input:
    w0_um, n, lambda_um = 500, 1.0, 0.532
    zr_m = rayleigh_range(w0_um, n, lambda_um)

    # Plot:
    r_um = np.linspace(-2 * w0_um, 2 * w0_um, 1000)
    z_m = np.linspace(-2 * zr_m, 2 * zr_m, 1000)
    r_um, z_m = np.meshgrid(r_um, z_m)
    Irz = intensity(r_um, z_m, zr_m, w0_um)
    r_mm = 1e-3 * r_um

    import matplotlib.pyplot as plt
    from matplotlib import cm
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(r_mm, z_m, Irz, cmap=cm.jet)
    ax.set_box_aspect((1.5, 3, 1))
    ax.set_title('Gaussian beam\n' +
                 '(w0_um=%0.2f, n=%0.2f, lambda_um=%0.3f, zr_m=%0.2f)'%(
                     (w0_um, n, lambda_um, zr_m)))
    ax.set_xlabel('r (mm)')
    ax.set_ylabel('z (m)')
    ax.set_zticks([])
    ax.set_zlim(0, 1)
    fig.colorbar(surf, shrink=0.5, label='Intensity', extend='both',
                 ticks=np.linspace(0, 1, 5))
    fig.savefig('intensity.png', dpi=150)
    plt.show()
