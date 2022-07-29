from solver import TimeLockPuzzleSolver
from timeit import timeit


def main():
    N = 146316494799812047511623076708218946420205748539793012358172922720474915105527936143913152868234855653659362702149685726946497663225575817296009946943300164053238818934292739741516716926800148512198028885552295620099510315701145312492185132376573874729991127362677325304713690683683766343670797779445517035741
    A = 2
    T = 800000

    print(f"{N=}")
    print(f"{A=} {T=}")

    solver = TimeLockPuzzleSolver(
        N=N,
        A=A,
        T=T
    )

    result = timeit(lambda: solver.run(
        in_progress_callback=lambda progress: print(f"{progress * 100:.1f}%"),
        progress_resolution=100
    ), number=1)
    print(f"Done in {result:.4f} seconds")
    

if __name__ == '__main__':
    main()
