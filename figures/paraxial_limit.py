import numpy as np

def paraxial_limit(n, lambda_um):
    w0_um = (3 * lambda_um) / (2 * np.pi * n)
    if isinstance(lambda_um, int) or isinstance(lambda_um, float):
        print('Paraxial limit:')
        print('(n=%0.2f, lambda_um=%0.2f)'%(n, lambda_um))
        print('w0_um=%0.2f'%w0_um)
    return w0_um

if __name__ == "__main__":
    # Input:
    n, lambda_um = 1.0, 0.532

    # Get value:
    w0_um = paraxial_limit(n, lambda_um)

    # Plot:
    lambda_um = np.linspace(0.4, 0.8, 1000)
    air_d0_um = 2 * paraxial_limit(1.00, lambda_um)
    oil_d0_um = 2 * paraxial_limit(1.51, lambda_um)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('Gaussian beam:\n paraxial limit')
    ax.set_ylabel('Diameter d0 (um)')
    ax.set_xlabel('Wavelength (um)')
    ax.plot(lambda_um, air_d0_um, label='air (n=1.00)',
            linestyle='-', color='k')
    ax.plot(lambda_um, oil_d0_um, label='oil (n=1.51)',
            linestyle='--', color='r')
    plt.legend(loc="upper left")
    fig.savefig('paraxial_limit.png', dpi=150)
    plt.show()
