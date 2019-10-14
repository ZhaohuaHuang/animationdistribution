"""
Demonstrate matplotlib animation of normal values.

Use random.noramlvariate to  generator numbers
in range(1, 25) with mean value of 12.5, standard deviation of 3.125
to simulate normal distribution. Dynamically
graph frequencies of normal distribution.

"""

from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys


def show_bar_chart(title, x_label, y_label, x_values, y_values, bar_toppers):
    """
    Display a bar chart.
    @param title the chart title.
    @param x_label the label for the x axis
    @param y_label the label for the y axis
    @param x_values the x values to plot
    @param y_values the y values to plot
    @param bar_toppers the text above each bar
    """

    plt.cla()  # clear old contents

    axes = sns.barplot(x_values, y_values, color='green')
    axes.set_title(title)
    axes.set(xlabel=x_label, ylabel=y_label)

    # Scale the y-axis by 10% to make room for text above the bars.
    axes.set_ylim(top=1.10 * max(y_values))

    # Display the topper text above each patch (bar).
    for bar, topper in zip(axes.patches, bar_toppers):
        text_x = bar.get_x() + bar.get_width() / 2
        text_y = bar.get_height()
        axes.text(text_x, text_y, topper,
                  fontsize=10, ha='center', va='bottom')


def update_frame(frame_number, count, normal_value, frequencies):
    """
    Update the bar plot contents for each animation frame.
    @param frame_number the frame number.
    @param count the count per frame.
    @param normal_value the random values.
    @param frequencies the list of random normal value frequencies.
    """

    # generate random value 'count' times and update the number frequencies.
    for _ in range(count):
        randomnumber=int(random.normalvariate(12.5,3.125))
        frequencies[randomnumber] += 1

        # Set the percentages for the bar tops.
    freq_sum = sum(frequencies)
    topper = [f'{freq:,}\n{freq / freq_sum:.2%}' for freq in frequencies]

    # Display the bar chart for this frame.
    show_bar_chart(f' Random number Frequencies for {freq_sum:,} Normal Distribution\n (Mean=12.5, Standard Deviation=3.125) ' +
                   f'(Frame {frame_number + 2})',
                   'Random Value', 'Frequency',
                   normal_value, frequencies, topper)


# Read command-line arguments for the number of frames
# and the number of counts per frame.
number_of_frames = int(sys.argv[1])
counts_per_frame = int(sys.argv[2])

# Create the figure for the animation.
sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Animated Normal Distribution')

values = list(range(1, 26))  # random values for display on the x-axis
frequencies = [0] * 25  # 0-25 list of values frequencies

# Configure and start the animation that calls function update_frame.
normal_animation = animation.FuncAnimation(
    figure, update_frame, repeat=False,
    frames=number_of_frames - 1, interval=25,
    fargs=(counts_per_frame, values, frequencies))

plt.show()