import matplotlib.pyplot as plt


def graph(input_vals, signal_vals, object_vals, model_vals):
    plt.plot(input_vals, signal_vals)
    plt.plot(input_vals, object_vals)

    plt.plot(input_vals, model_vals, 'r.')
    plt.show()
