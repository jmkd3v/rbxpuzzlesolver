from typing import Optional

DEFAULT_PROGRESS_RESOLUTION = 1000


class TimeLockPuzzleSolver:
    def __init__(
            self,
            N: int,
            A: int,
            T: int
    ):
        self.N = N
        self.A = A
        self.T = T

        self.cur_base = self.A
        self.cur_T = 0

    def run(self, in_progress_callback=None, progress_resolution: int = DEFAULT_PROGRESS_RESOLUTION) -> int:
        batch_size = max(1, self.T // progress_resolution)
        while not self.done:
            self.do_repeated_squaring(batch_size)
            if in_progress_callback:
                in_progress_callback(self.progress)

        return self.answer

    def do_repeated_squaring(self, iterations: Optional[int] = None):
        target_T = self.T if iterations is None else min(self.T, self.cur_T + iterations)
        while self.cur_T < target_T:
            self.cur_base = pow(self.cur_base, 2) % self.N
            self.cur_T += 1

    @property
    def answer(self) -> Optional[int]:
        if not self.done:
            return None

        return self.cur_base

    @property
    def progress(self):
        return self.cur_T / self.T

    @property
    def done(self):
        return self.cur_T == self.T
