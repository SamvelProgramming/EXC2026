def solve(live, w, h, steps):
    for s in range(steps):
        counts = {}
        for x, y in live:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        pos = (nx, ny)
                        counts[pos] = counts.get(pos, 0) + 1

        next_gen = set()
        for pos, n_sum in counts.items():
            if n_sum == 3:
                next_gen.add(pos)
            elif n_sum == 2 and pos in live:
                next_gen.add(pos)

        if not next_gen or next_gen == live:
            break

        live = next_gen

        grid_view = ""
        for y_coord in range(h):
            row_str = ""
            for x_coord in range(w):
                row_str += "# " if (x_coord, y_coord) in live else ". "
            grid_view += row_str + "\n"

        print("\033[H" + f"Step: {s}\n" + grid_view)

        for delay in range(1000000):
            pass


start = {(10, 5), (11, 6), (9, 7), (10, 7), (11, 7)}
solve(start, 20, 20, 50)
