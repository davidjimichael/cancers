from sklearn import datasets
import matplotlib.pyplot as plt

def example_pyplot():
    iris = datasets.load_iris()
    print(iris.feature_names)

    _, ax = plt.subplots()

    scatter = plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
    ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])

    _ = ax.legend(
        scatter.legend_elements()[0], iris.target_names, loc="lower right", title="flowers"
    )

    plt.title(label="iris dataset", fontdict={"font":"courier new"})
    plt.show()