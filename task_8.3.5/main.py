import math


def test_all_tasks():
    output_lines = ["Завдання 8.3.5 - Результати тестування\n"]

    # a) 
    output_lines.append("\na) Послідовність x_k = x^(2k)/(2k)!")
    with open('input_a.txt', encoding='utf-8') as f:
        for line in f:
            x, k = map(float, line.strip().split())
            result = x ** (2 * int(k)) / math.factorial(2 * int(k))
            output_lines.append(f"x = {x}, k = {int(k)}: {result}")

    # b) 
    output_lines.append("\nb) Добуток P_n = продукт(1 + 1/k^2)")  
    with open('input_b.txt', encoding='utf-8') as f:
        for line in f:
            n = int(line.strip())
            product = 1.0
            for k in range(1, n + 1):
                product *= (1 + 1 / k ** 2)
            output_lines.append(f"n = {n}: {product}")

    # c) 
    output_lines.append("\nc) Визначник тридіагональної матриці")
    with open('input_c.txt', encoding='utf-8') as f:
        for line in f:
            n, a, b = map(float, line.strip().split())
            if n == 1:
                det = a + b
            elif n == 2:
                det = (a + b) ** 2 - a * b
            else:
                d_prev_prev, d_prev = a + b, (a + b) ** 2 - a * b
                for _ in range(3, int(n) + 1):
                    d_current = (a + b) * d_prev - a * b * d_prev_prev
                    d_prev_prev, d_prev = d_prev, d_current
                det = d_prev
            output_lines.append(f"n = {int(n)}, a = {a}, b = {b}: {det}")

    # d) 
    output_lines.append("\nd) Сума S_n = Σ(a_k/2^k)")
    with open('input_d.txt', encoding='utf-8') as f:
        for line in f:
            n = int(line.strip())
            if n >= 1:
                a = [0, 1, 1, 1]  
                total = sum(a[k] / (2 ** k) for k in range(1, min(n + 1, 4)))
                for k in range(4, n + 1):
                    a_k = a[k - 1] + a[k - 3]
                    a.append(a_k)
                    total += a_k / (2 ** k)
                output_lines.append(f"n = {n}: {total}")

    # e) 
    output_lines.append("\ne) Ряд Тейлора для ln((1+x)/(1-x))")
    with open('input_e.txt', encoding='utf-8') as f:
        for line in f:
            x, eps = map(float, line.strip().split())
            result = 0.0
            k = 1
            while True:
                term = 2 * (x ** k / k)
                result += term
                if abs(term) < eps:
                    break
                k += 2
            exact = math.log((1 + x) / (1 - x))
            output_lines.append(
                f"x = {x}, ε = {eps}:\n"
                f"  Наближене: {result:.6f}\n"
                f"  Точне: {exact:.6f}\n"
                f"  Похибка: {abs(result - exact):.6f}"
            )

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))


if __name__ == "__main__":
    test_all_tasks()
