from analytics import Research
import config

def make_report():
    research = Research(config.file)
    lines = research.file_reader()
    analytics = research.Analytics()

    # counts = Research.Calculations.counts(lines)
    counts = analytics.counts(lines)

    heads, tails = counts
    fractions = analytics.fractions(*counts)
    res_rnd = analytics.predict_random(3)

    res = f"Report\nWe have made {heads + tails} observations from tossing a coin: " \
          f"{tails} of them were tails and {heads} of them were heads. " \
          f"The probabilities are {round(fractions[0], 2)}% and {round(fractions[1], 2)}%, respectively. " \
          f"Our forecast is that in the next {config.num_of_steps} observations " \
          f"we will have: {res_rnd.count([1, 0])} tail and {res_rnd.count([0, 1])} heads."
    analytics.save_file(res, "report", "txt")


if __name__ == '__main__':
    make_report()
