import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.plot(midterm_kr, final_kr, 'ro')
    plt.plot(midterm_en, final_en, 'b+')
    plt.xlabel('midterm scores')
    plt.ylabel('final scores')
    plt.xlim(0,125)
    plt.ylim(0,100)
    plt.grid(True)
    plt.legend(('korean', 'english'))
    plt.show()

    # TODO) Plot total scores as a histogram
    plt.hist(total_kr, bins = 20, range=[0,100], color='red', alpha = 0.5)
    plt.hist(total_en, bins = 20, range=[0,100], color='blue', alpha = 0.5)
    plt.xlabel('total scores')
    plt.ylabel('the number of student')
    plt.legend(('korean', 'english'))
    plt.show()