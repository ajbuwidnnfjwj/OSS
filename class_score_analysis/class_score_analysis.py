def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        data = [list(map(int, score.split(', '))) for score in file.read().splitlines()[1:]]
    return data


def calc_weighted_average(data_2d, weight):
    average = [score[0] * weight[0] + score[1] * weight[1] for score in data_2d]
    return average


def analyze_data(data_1d):
    # preprocessing data
    data_1d.sort()
    summation = sum(data_1d)
    length = len(data_1d)
    # mean
    mean = summation / length
    # variance
    var = sum([(i - mean) ** 2 for i in data_1d]) / length
    # median
    median = (data_1d[length / 2] + data_1d[length / 2 + 1]) / 2 if length % 2 == 0 else data_1d[length // 2]
    return mean, var, median, min(data_1d), max(data_1d)


if __name__ == '__main__':
    data = read_data('./data/class_score_en.csv')
    if data and len(data[0]) == 2:  # Check 'data' is valid
        average = calc_weighted_average(data, [40 / 125, 60 / 100])

        # Write the analysis report as a markdown file
        with open('./class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final': [f_score for _, f_score in data],
                'Average': average}
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
