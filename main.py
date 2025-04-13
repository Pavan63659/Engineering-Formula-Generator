from formulas import newtons_second_law, ideal_gas_law, stress, strain, electrical_power, work_done, efficiency, bernoulli

f, form = newtons_second_law(10, 3)
print(f"Force: {f} N, Formula: {form}")

stress_val, s_form = stress(200, 10)
print(f"Stress: {stress_val} Pa, Formula: {s_form}")

power, p_form = electrical_power(current=2, resistance=10)
print(f"Power: {power} W, Formula: {p_form}")