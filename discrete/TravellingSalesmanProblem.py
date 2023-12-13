from numpy import array
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.backend_bases import PickEvent
from datalayer.Path import Path


class TravellingSalesmanProblem:
    """Visualize the Traveling Salesman Problem"""

    CLR_POINT = "#eb343a"
    CLR_PATH = [
        "#eb343a", "#db34eb", "#5b34eb", "#34b4eb",
        "#34eb4c", "#ebe534", "#eb9234",
    ]

    def __init__(
            self,
            points: list[tuple[int, int]],
            paths: list[Path] = None
    ) -> None:
        """Initializes the problem, outputs its data using graphics."""
        self.__points = points
        self.__paths = paths
        self.__fig, self.__ax = plt.subplots(num=f"Travelling Salesman Problem")
        self.__show()

    def get_points(self) -> list[tuple[int, int]]:
        """Getter to get the list of 2D points of the initialized problem."""
        return self.__points

    def get_paths(self) -> list[Path]:
        """Getter to get the list of paths of the initialized problem."""
        return self.__paths

    def __draw_points(self) -> None:
        """Draws 2D points and their coordinates on the canvas."""
        self.__ax.scatter(
            *array(self.__points).T,
            zorder=1,
            color=TravellingSalesmanProblem.CLR_POINT,
            label=f"Points ({len(self.__points)})",
        )
        for i, p in enumerate(self.__points):
            plt.annotate(
                i + 1,
                p,
                ha="center",
                textcoords="offset points",
                xytext=(0, 4),
                fontsize=8,
            )
            plt.annotate(
                f"({p[0]}; {p[1]})",
                p,
                ha="center",
                va="top",
                textcoords="offset points",
                xytext=(0, -4),
                fontsize=6,
            )

    def __draw_paths(self) -> list[Line2D]:
        """Draws all given paths on the canvas."""
        lines = []
        if self.__paths:
            for i, path in enumerate(self.__paths):
                print(f'Path founded, by {path.name} is {path.indices},'
                      f' and its length={path.length}')
                points = [self.__points[i] for i in path.indices]
                (l,) = plt.plot(
                    *array(points).T,
                    ls="--",
                    zorder=0,
                    color=TravellingSalesmanProblem.CLR_PATH[
                        i % len(TravellingSalesmanProblem.CLR_PATH)],
                    label=f"{path.name} ({path.length:.2f})",
                )
                lines.append(l)
        return lines

    def __draw_legend(self, lines: list[Line2D]) -> None:
        """Draws the legend on the canvas."""
        if lines:
            self.__ax.set_title(
                "Tip: Click on the legend line(s) to turn the path ON / OFF",
                fontsize=10, loc="left",
            )
            legend = self.__ax.legend()
            lined = {}
            for legline, origline in zip(legend.get_lines(), lines):
                legline.set_picker(True)
                lined[legline] = origline

            def on_pick(event: PickEvent) -> None:
                legline = event.artist
                origline = lined[legline]
                visible = not origline.get_visible()
                origline.set_visible(visible)
                legline.set_alpha(1.0 if visible else 0.2)
                self.__fig.canvas.draw()

            self.__fig.canvas.mpl_connect("pick_event", on_pick)
        else:
            self.__ax.legend()

    def __show(self) -> None:
        """Shows the canvas with the drawn data."""
        self.__draw_points()
        lines = self.__draw_paths()
        self.__draw_legend(lines=lines)
        plt.show()
