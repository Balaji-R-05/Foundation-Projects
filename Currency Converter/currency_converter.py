def convert_rupees_to_paisa(rupees):
    paisa = int(rupees * 100)
    return paisa

# Example usage:
rupees_amount = float(input("Enter rupees amount: "))
paisa_result = convert_rupees_to_paisa(rupees_amount)

print(f"{rupees_amount} rupees is equal to {paisa_result} paisa.")
